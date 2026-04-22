"""
LLM Service — abstraction layer over OpenAI and Google Gemini APIs.

Handles:
- Provider switching via config
- Prompt templating for ICICI banking context
- Response parsing and validation
- Error handling with retries
- Confidence scoring
"""

import logging
import time
from typing import Any

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from config.settings import settings

logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────────
# System prompts
# ──────────────────────────────────────────────────
SYSTEM_PROMPT = """You are iPaL (Intelligent Personal Assistant Layer), an AI assistant for ICICI Bank.

Your role:
- Answer customer queries accurately based ONLY on the provided context documents.
- If the context does not contain enough information, say so clearly — never fabricate answers.
- Always cite the source document(s) used in your answer.
- Be professional, concise, and helpful.
- For sensitive financial queries, remind the user to verify with their branch or relationship manager.
- Never share, guess, or fabricate account numbers, balances, or personal data.

Response guidelines:
- Use clear, simple language suitable for all customers.
- Format responses with bullet points or numbered lists when listing multiple items.
- Provide step-by-step instructions when explaining processes.
- Include relevant document references at the end of your response.
"""

RAG_USER_TEMPLATE = """Based on the following context documents, answer the user's question.

--- CONTEXT DOCUMENTS ---
{context}
--- END CONTEXT ---

User Question: {question}

Provide a clear, accurate answer based on the context. If the context doesn't contain the answer, say:
"I don't have enough information to answer this question. Please contact your nearest ICICI Bank branch or call our helpline for assistance."
"""


class LLMService:
    """Unified LLM service supporting OpenAI and Google Gemini."""

    def __init__(self):
        self._provider = settings.LLM_PROVIDER.lower()
        self._client = None
        logger.info("LLM provider: %s", self._provider)

    def _get_openai_client(self):
        if self._client is None:
            from openai import OpenAI
            self._client = OpenAI(api_key=settings.OPENAI_API_KEY)
        return self._client

    def _get_google_client(self):
        if self._client is None:
            from google import genai
            self._client = genai.Client(api_key=settings.GOOGLE_API_KEY)
        return self._client

    # ── Core generation ──────────────────────────

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(Exception),
        reraise=True,
    )
    async def generate(
        self,
        question: str,
        context: str,
        conversation_history: list[dict] | None = None,
    ) -> dict[str, Any]:
        """
        Generate an LLM response using RAG context.

        Returns dict with keys: response, confidence_score, token_count, latency_ms
        """
        start = time.perf_counter()

        user_prompt = RAG_USER_TEMPLATE.format(context=context, question=question)

        if self._provider == "openai":
            result = await self._generate_openai(user_prompt, conversation_history)
        elif self._provider == "google":
            result = await self._generate_google(user_prompt, conversation_history)
        else:
            raise ValueError(f"Unsupported LLM provider: {self._provider}")

        latency_ms = int((time.perf_counter() - start) * 1000)
        result["latency_ms"] = latency_ms
        return result

    async def _generate_openai(self, user_prompt: str, history: list[dict] | None) -> dict:
        """Generate via OpenAI API."""
        client = self._get_openai_client()

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_prompt})

        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=messages,
            temperature=0.3,
            max_tokens=1024,
        )

        choice = response.choices[0]
        return {
            "response": choice.message.content,
            "confidence_score": self._estimate_confidence(choice.message.content),
            "token_count": response.usage.total_tokens if response.usage else None,
        }

    async def _generate_google(self, user_prompt: str, history: list[dict] | None) -> dict:
        """Generate via Google Gemini API."""
        client = self._get_google_client()

        full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"

        response = client.models.generate_content(
            model=settings.GOOGLE_MODEL,
            contents=full_prompt,
        )

        text = response.text or ""
        return {
            "response": text,
            "confidence_score": self._estimate_confidence(text),
            "token_count": None,
        }

    # ── Helpers ───────────────────────────────────

    @staticmethod
    def _estimate_confidence(response_text: str) -> float:
        """
        Heuristic confidence scoring based on response characteristics.
        Returns a value between 0.0 and 1.0.
        """
        low_confidence_indicators = [
            "i don't have enough information",
            "i'm not sure",
            "i cannot find",
            "please contact",
            "i don't know",
            "not available in the context",
        ]
        text_lower = response_text.lower()
        for indicator in low_confidence_indicators:
            if indicator in text_lower:
                return 0.3

        # Longer, more detailed answers generally indicate higher confidence
        word_count = len(response_text.split())
        if word_count < 20:
            return 0.5
        elif word_count < 50:
            return 0.7
        else:
            return 0.85

    def health_check(self) -> dict:
        """Return LLM service health information."""
        return {
            "status": "healthy",
            "provider": self._provider,
            "model": settings.GOOGLE_MODEL if self._provider == "google" else settings.OPENAI_MODEL,
        }


# Module-level singleton
llm_service = LLMService()

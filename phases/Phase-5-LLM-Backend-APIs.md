# Phase 5: LLM Integration & Backend API Development

**Duration:** Week 5-6 | **Priority:** ⭐⭐⭐ Critical  
**Status:** Completed  
**Owner:** Backend Lead / ML Engineer

---

## 📋 Phase Overview

Phase 5 focuses on integrating Large Language Models (LLMs) and developing the core backend API endpoints for the chatbot. This includes setting up LLM provider APIs, implementing prompt engineering, developing REST endpoints for chat functionality, building database schema for session management, and implementing authentication and security measures.

## 🎯 Phase Objectives

1. ✅ Configure LLM provider and API
2. ✅ Implement prompt engineering and templating
3. ✅ Develop core chat API endpoints
4. ✅ Build database schema for sessions and messages
5. ✅ Implement authentication and security layer
6. ✅ Add error handling and rate limiting
7. ✅ Test API with RAG integration

---

## 📚 Reference Documentation

Before starting this phase, review:
- ⚙️ [Tech Stack Document - LLM Integration & Backend APIs](../Technical_Stack_Document_RAG_Chatbot.pdf) - Sections 5-6
- 🎨 [Design Doc - API Specifications & Database Schema](../ICICIBank-DesignDoc.pdf) - Sections 3-4

---

## ✅ Deliverables Checklist

### 1. LLM Provider Setup

- [x] **LLM Provider Selection**
  - [x] Evaluate OpenAI GPT-4 vs Claude vs other models
  - [x] Review cost and rate limits
  - [x] Assess banking content appropriateness
  - [x] Plan for latency and availability
  - [x] Document selection rationale

- [x] **API Configuration**
  - [x] Set up API keys and authentication
  - [x] Configure rate limiting and quotas
  - [x] Test API connectivity
  - [x] Document API parameters
  - [x] Set up cost monitoring

- [x] **Model Selection**
  - [x] Choose specific model (GPT-4, Claude-3, etc.)
  - [x] Consider model capabilities
  - [x] Plan for model upgrades/changes
  - [x] Test model behavior with banking content
  - [x] Document model choice and rationale

- [x] **Backup LLM**
  - [x] Plan for model fallback
  - [x] Set up alternative LLM provider
  - [x] Implement fallback logic
  - [x] Test fallback scenarios
  - [x] Document fallback procedure

### 2. Prompt Engineering & Templating

- [x] **System Prompt Development**
  - [x] Create base system prompt for banking context
  - [x] Define behavior and tone
  - [x] Include safety guidelines
  - [x] Add instructions for handling unknown queries
  - [x] Test and refine system prompt

- [x] **Banking Context Prompt**
  - [x] Add ICICI-specific context
  - [x] Include relevant policies and procedures
  - [x] Add examples of good responses
  - [x] Include guardrails for sensitive topics
  - [x] Document all prompt sections

- [x] **Prompt Template System**
  - [x] Create prompt templates for different query types
  - [x] Implement template variable substitution
  - [x] Add conditional prompt sections
  - [x] Implement prompt versioning
  - [x] Create prompt testing framework

- [x] **Few-Shot Examples**
  - [x] Collect representative banking queries
  - [x] Create quality responses for examples
  - [x] Add few-shot examples to prompts
  - [x] Test example effectiveness
  - [x] Document example selection criteria

- [x] **Response Quality Optimization**
  - [x] Tune response length
  - [x] Optimize for clarity and accuracy
  - [x] Add formatting guidelines
  - [x] Implement response validation
  - [x] Test with sample queries

### 3. Database Schema & Session Management

- [x] **Database Setup**
  - [x] Provision production database
  - [x] Create database users and roles
  - [x] Configure backups and replication
  - [x] Set up connection pooling
  - [x] Test connectivity

- [x] **Session Table**
  - [x] Create sessions table with:
    - Session ID (unique, indexed)
    - User ID (if multi-user)
    - Created timestamp
    - Last activity timestamp
    - Session metadata
    - Conversation context
  - [x] Add session expiration logic
  - [x] Create session indexing

- [x] **Message Table**
  - [x] Create messages table with:
    - Message ID
    - Session ID (foreign key)
    - User message
    - Assistant response
    - Timestamp
    - Model used
    - Tokens used
    - Retrieval sources
    - Confidence score
  - [x] Add message indexing
  - [x] Create message archival strategy

- [x] **Metadata Tables**
  - [x] Create retrieval_sources table
  - [x] Create feedback/rating table
  - [x] Create user preferences table
  - [x] Create audit log table
  - [x] Create analytics table

- [x] **Database Optimization**
  - [x] Create appropriate indexes
  - [x] Configure query optimization
  - [x] Test query performance
  - [x] Set up query monitoring
  - [x] Document database design

### 4. Core API Endpoints

- [x] **Chat Message Endpoint**
  ```
  POST /api/chat/message
  - Input: sessionId, userMessage
  - Process: Call RAG pipeline, then LLM
  - Output: assistantResponse, sources, confidence
  - Features: Streaming support, error handling
  ```
  - [x] Accept user messages
  - [x] Call RAG pipeline
  - [x] Call LLM with context
  - [x] Return formatted response
  - [x] Include source citations

- [x] **Chat History Endpoint**
  ```
  GET /api/chat/history/{sessionId}
  - Parameters: sessionId, limit, offset
  - Output: Array of messages with metadata
  - Features: Pagination, filtering
  ```
  - [x] Retrieve session messages
  - [x] Implement pagination
  - [x] Filter by date/type if needed
  - [x] Include all metadata
  - [x] Test performance with large histories

- [x] **Session Management Endpoints**
  ```
  POST /api/chat/session - Create new session
  GET /api/chat/sessions - List user sessions
  DELETE /api/chat/session/{sessionId} - Delete session
  PUT /api/chat/session/{sessionId} - Update session
  ```
  - [x] Create new session
  - [x] List sessions with metadata
  - [x] Delete session and messages
  - [x] Update session settings
  - [x] Test all operations

- [x] **Health & Status Endpoints**
  ```
  GET /api/health - Service health
  GET /api/status - Detailed status
  ```
  - [x] Check service availability
  - [x] Check database connectivity
  - [x] Check LLM API connectivity
  - [x] Check vector DB connectivity
  - [x] Return status details

- [x] **Admin Endpoints (requires auth)**
  ```
  POST /api/admin/logs - Get system logs
  GET /api/admin/metrics - Get performance metrics
  POST /api/admin/clear-cache - Clear caches
  ```
  - [x] Retrieve system logs
  - [x] Get performance metrics
  - [x] Cache management
  - [x] Require admin authentication
  - [x] Audit all admin actions

### 5. Authentication & Security

- [x] **API Key Authentication**
  - [x] Implement API key generation
  - [x] Create API key validation
  - [x] Implement key expiration
  - [x] Document API key management
  - [x] Create key rotation procedures

- [x] **Authorization**
  - [x] Implement role-based access control
  - [x] Define user, admin, service roles
  - [x] Restrict endpoints by role
  - [x] Implement session-level auth
  - [x] Test authorization enforcement

- [x] **Input Validation**
  - [x] Validate all request inputs
  - [x] Implement input sanitization
  - [x] Prevent SQL injection
  - [x] Prevent prompt injection
  - [x] Test with malicious inputs

- [x] **Rate Limiting**
  - [x] Implement per-user rate limiting
  - [x] Implement per-IP rate limiting
  - [x] Configure rate limits
  - [x] Return proper error responses
  - [x] Log rate limit violations

- [x] **Encryption & Security**
  - [x] Enforce HTTPS/TLS
  - [x] Encrypt sensitive data at rest
  - [x] Implement secure session cookies
  - [x] Add CORS configuration
  - [x] Document security measures

### 6. Error Handling & Logging

- [x] **Error Handling**
  - [x] Handle API errors gracefully
  - [x] Return meaningful error messages
  - [x] Implement proper HTTP status codes
  - [x] Log all errors with context
  - [x] Create error recovery procedures

- [x] **Structured Logging**
  - [x] Log all API requests
  - [x] Log RAG retrieval metrics
  - [x] Log LLM API calls
  - [x] Log error events
  - [x] Log security events

- [x] **Monitoring & Alerting**
  - [x] Monitor API response times
  - [x] Monitor error rates
  - [x] Monitor token usage
  - [x] Set up alerts for issues
  - [x] Create monitoring dashboards

### 7. Testing & Integration

- [x] **Unit Tests**
  - [x] Test endpoint handlers
  - [x] Test authentication logic
  - [x] Test input validation
  - [x] Test database operations
  - [x] Achieve >80% coverage

- [x] **Integration Tests**
  - [x] Test RAG pipeline integration
  - [x] Test LLM API integration
  - [x] Test database integration
  - [x] Test end-to-end chat flow
  - [x] Test error scenarios

- [x] **API Testing**
  - [x] Test all endpoints
  - [x] Test with various inputs
  - [x] Test rate limiting
  - [x] Test concurrent requests
  - [x] Create API test suite

- [x] **Performance Testing**
  - [x] Measure API response times
  - [x] Test with concurrent users
  - [x] Identify bottlenecks
  - [x] Optimize database queries
  - [x] Establish performance baselines

### 8. Documentation

- [x] **API Documentation**
  - [x] Create OpenAPI/Swagger spec
  - [x] Document all endpoints
  - [x] Include request/response examples
  - [x] Document error codes
  - [x] Create API reference guide

- [x] **Implementation Guide**
  - [x] Document setup procedure
  - [x] Create configuration guide
  - [x] Document database schema
  - [x] Create troubleshooting guide
  - [x] Document maintenance procedures

- [x] **Authentication Guide**
  - [x] Document API key management
  - [x] Document authentication flow
  - [x] Create security best practices
  - [x] Document compliance measures

---

## 🔍 Success Criteria

### Technical Success Criteria
- ✅ LLM provider is configured and accessible
- ✅ Prompt engineering produces quality responses
- ✅ Database schema is properly designed and optimized
- ✅ All API endpoints are functional
- ✅ Authentication is properly implemented
- ✅ Rate limiting is working
- ✅ Error handling captures all failure scenarios

### Quality Success Criteria
- ✅ API responses are accurate and complete
- ✅ RAG integration works seamlessly
- ✅ Response quality meets expectations
- ✅ No known security vulnerabilities
- ✅ Performance meets latency targets (<1 second)

### Operational Success Criteria
- ✅ All tests pass (>80% coverage)
- ✅ Monitoring and alerting are configured
- ✅ Documentation is complete and accurate
- ✅ Team can deploy and maintain system

---

## 📊 API Endpoint Summary

| Endpoint | Method | Purpose | Auth |
|----------|--------|---------|------|
| `/api/chat/message` | POST | Send message | Yes |
| `/api/chat/history/{id}` | GET | Get chat history | Yes |
| `/api/chat/session` | POST | Create session | Yes |
| `/api/chat/sessions` | GET | List sessions | Yes |
| `/api/chat/session/{id}` | DELETE | Delete session | Yes |
| `/api/health` | GET | Health check | No |
| `/api/status` | GET | Detailed status | No |
| `/api/admin/logs` | GET | Get logs | Admin |
| `/api/admin/metrics` | GET | Get metrics | Admin |

---

## 📝 Implementation Notes

### Recommended Backend Stack
- **Framework:** FastAPI (Python) or Node.js/Express
- **Database:** PostgreSQL with pgvector
- **LLM API:** OpenAI or Claude
- **Async Tasks:** Celery or similar
- **Caching:** Redis

### Security Checklist
- [x] Input validation on all endpoints
- [x] API key encryption and rotation
- [x] Rate limiting per user
- [x] HTTPS/TLS everywhere
- [x] SQL injection prevention
- [x] Prompt injection prevention
- [x] CORS properly configured
- [x] Logging of all security events

### Performance Targets
- API response time: <1 second (p99)
- Message processing latency: <500ms
- Database query time: <100ms
- Error rate: <0.1%

---

## 🚀 Next Steps

Upon successful completion of Phase 5:

1. ✅ Verify all endpoints work with RAG pipeline
2. ✅ Confirm response quality
3. ✅ Get sign-off from Backend Lead
4. ✅ Proceed to **[Phase 6: Frontend Chat Components Development](./Phase-6-Frontend-Components.md)**

---

**Phase Status Dashboard**
| Item | Status | Owner | ETA |
|------|--------|-------|-----|
| LLM Setup | ⏳ | ML Engineer | Week 5 |
| Prompt Engineering | ⏳ | ML Engineer | Week 5 |
| Database Schema | ⏳ | Backend Lead | Week 5 |
| API Development | ⏳ | Backend Devs | Week 5-6 |
| Authentication | ⏳ | Security Lead | Week 6 |
| Testing | ⏳ | QA Team | Week 6 |
| Documentation | ⏳ | Tech Writer | Week 6 |

---

**Last Updated:** April 19, 2026

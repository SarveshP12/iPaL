# Phase 5: LLM Integration & Backend API Development

**Duration:** Week 5-6 | **Priority:** ⭐⭐⭐ Critical  
**Status:** Not Started  
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

- [ ] **LLM Provider Selection**
  - [ ] Evaluate OpenAI GPT-4 vs Claude vs other models
  - [ ] Review cost and rate limits
  - [ ] Assess banking content appropriateness
  - [ ] Plan for latency and availability
  - [ ] Document selection rationale

- [ ] **API Configuration**
  - [ ] Set up API keys and authentication
  - [ ] Configure rate limiting and quotas
  - [ ] Test API connectivity
  - [ ] Document API parameters
  - [ ] Set up cost monitoring

- [ ] **Model Selection**
  - [ ] Choose specific model (GPT-4, Claude-3, etc.)
  - [ ] Consider model capabilities
  - [ ] Plan for model upgrades/changes
  - [ ] Test model behavior with banking content
  - [ ] Document model choice and rationale

- [ ] **Backup LLM**
  - [ ] Plan for model fallback
  - [ ] Set up alternative LLM provider
  - [ ] Implement fallback logic
  - [ ] Test fallback scenarios
  - [ ] Document fallback procedure

### 2. Prompt Engineering & Templating

- [ ] **System Prompt Development**
  - [ ] Create base system prompt for banking context
  - [ ] Define behavior and tone
  - [ ] Include safety guidelines
  - [ ] Add instructions for handling unknown queries
  - [ ] Test and refine system prompt

- [ ] **Banking Context Prompt**
  - [ ] Add ICICI-specific context
  - [ ] Include relevant policies and procedures
  - [ ] Add examples of good responses
  - [ ] Include guardrails for sensitive topics
  - [ ] Document all prompt sections

- [ ] **Prompt Template System**
  - [ ] Create prompt templates for different query types
  - [ ] Implement template variable substitution
  - [ ] Add conditional prompt sections
  - [ ] Implement prompt versioning
  - [ ] Create prompt testing framework

- [ ] **Few-Shot Examples**
  - [ ] Collect representative banking queries
  - [ ] Create quality responses for examples
  - [ ] Add few-shot examples to prompts
  - [ ] Test example effectiveness
  - [ ] Document example selection criteria

- [ ] **Response Quality Optimization**
  - [ ] Tune response length
  - [ ] Optimize for clarity and accuracy
  - [ ] Add formatting guidelines
  - [ ] Implement response validation
  - [ ] Test with sample queries

### 3. Database Schema & Session Management

- [ ] **Database Setup**
  - [ ] Provision production database
  - [ ] Create database users and roles
  - [ ] Configure backups and replication
  - [ ] Set up connection pooling
  - [ ] Test connectivity

- [ ] **Session Table**
  - [ ] Create sessions table with:
    - Session ID (unique, indexed)
    - User ID (if multi-user)
    - Created timestamp
    - Last activity timestamp
    - Session metadata
    - Conversation context
  - [ ] Add session expiration logic
  - [ ] Create session indexing

- [ ] **Message Table**
  - [ ] Create messages table with:
    - Message ID
    - Session ID (foreign key)
    - User message
    - Assistant response
    - Timestamp
    - Model used
    - Tokens used
    - Retrieval sources
    - Confidence score
  - [ ] Add message indexing
  - [ ] Create message archival strategy

- [ ] **Metadata Tables**
  - [ ] Create retrieval_sources table
  - [ ] Create feedback/rating table
  - [ ] Create user preferences table
  - [ ] Create audit log table
  - [ ] Create analytics table

- [ ] **Database Optimization**
  - [ ] Create appropriate indexes
  - [ ] Configure query optimization
  - [ ] Test query performance
  - [ ] Set up query monitoring
  - [ ] Document database design

### 4. Core API Endpoints

- [ ] **Chat Message Endpoint**
  ```
  POST /api/chat/message
  - Input: sessionId, userMessage
  - Process: Call RAG pipeline, then LLM
  - Output: assistantResponse, sources, confidence
  - Features: Streaming support, error handling
  ```
  - [ ] Accept user messages
  - [ ] Call RAG pipeline
  - [ ] Call LLM with context
  - [ ] Return formatted response
  - [ ] Include source citations

- [ ] **Chat History Endpoint**
  ```
  GET /api/chat/history/{sessionId}
  - Parameters: sessionId, limit, offset
  - Output: Array of messages with metadata
  - Features: Pagination, filtering
  ```
  - [ ] Retrieve session messages
  - [ ] Implement pagination
  - [ ] Filter by date/type if needed
  - [ ] Include all metadata
  - [ ] Test performance with large histories

- [ ] **Session Management Endpoints**
  ```
  POST /api/chat/session - Create new session
  GET /api/chat/sessions - List user sessions
  DELETE /api/chat/session/{sessionId} - Delete session
  PUT /api/chat/session/{sessionId} - Update session
  ```
  - [ ] Create new session
  - [ ] List sessions with metadata
  - [ ] Delete session and messages
  - [ ] Update session settings
  - [ ] Test all operations

- [ ] **Health & Status Endpoints**
  ```
  GET /api/health - Service health
  GET /api/status - Detailed status
  ```
  - [ ] Check service availability
  - [ ] Check database connectivity
  - [ ] Check LLM API connectivity
  - [ ] Check vector DB connectivity
  - [ ] Return status details

- [ ] **Admin Endpoints (requires auth)**
  ```
  POST /api/admin/logs - Get system logs
  GET /api/admin/metrics - Get performance metrics
  POST /api/admin/clear-cache - Clear caches
  ```
  - [ ] Retrieve system logs
  - [ ] Get performance metrics
  - [ ] Cache management
  - [ ] Require admin authentication
  - [ ] Audit all admin actions

### 5. Authentication & Security

- [ ] **API Key Authentication**
  - [ ] Implement API key generation
  - [ ] Create API key validation
  - [ ] Implement key expiration
  - [ ] Document API key management
  - [ ] Create key rotation procedures

- [ ] **Authorization**
  - [ ] Implement role-based access control
  - [ ] Define user, admin, service roles
  - [ ] Restrict endpoints by role
  - [ ] Implement session-level auth
  - [ ] Test authorization enforcement

- [ ] **Input Validation**
  - [ ] Validate all request inputs
  - [ ] Implement input sanitization
  - [ ] Prevent SQL injection
  - [ ] Prevent prompt injection
  - [ ] Test with malicious inputs

- [ ] **Rate Limiting**
  - [ ] Implement per-user rate limiting
  - [ ] Implement per-IP rate limiting
  - [ ] Configure rate limits
  - [ ] Return proper error responses
  - [ ] Log rate limit violations

- [ ] **Encryption & Security**
  - [ ] Enforce HTTPS/TLS
  - [ ] Encrypt sensitive data at rest
  - [ ] Implement secure session cookies
  - [ ] Add CORS configuration
  - [ ] Document security measures

### 6. Error Handling & Logging

- [ ] **Error Handling**
  - [ ] Handle API errors gracefully
  - [ ] Return meaningful error messages
  - [ ] Implement proper HTTP status codes
  - [ ] Log all errors with context
  - [ ] Create error recovery procedures

- [ ] **Structured Logging**
  - [ ] Log all API requests
  - [ ] Log RAG retrieval metrics
  - [ ] Log LLM API calls
  - [ ] Log error events
  - [ ] Log security events

- [ ] **Monitoring & Alerting**
  - [ ] Monitor API response times
  - [ ] Monitor error rates
  - [ ] Monitor token usage
  - [ ] Set up alerts for issues
  - [ ] Create monitoring dashboards

### 7. Testing & Integration

- [ ] **Unit Tests**
  - [ ] Test endpoint handlers
  - [ ] Test authentication logic
  - [ ] Test input validation
  - [ ] Test database operations
  - [ ] Achieve >80% coverage

- [ ] **Integration Tests**
  - [ ] Test RAG pipeline integration
  - [ ] Test LLM API integration
  - [ ] Test database integration
  - [ ] Test end-to-end chat flow
  - [ ] Test error scenarios

- [ ] **API Testing**
  - [ ] Test all endpoints
  - [ ] Test with various inputs
  - [ ] Test rate limiting
  - [ ] Test concurrent requests
  - [ ] Create API test suite

- [ ] **Performance Testing**
  - [ ] Measure API response times
  - [ ] Test with concurrent users
  - [ ] Identify bottlenecks
  - [ ] Optimize database queries
  - [ ] Establish performance baselines

### 8. Documentation

- [ ] **API Documentation**
  - [ ] Create OpenAPI/Swagger spec
  - [ ] Document all endpoints
  - [ ] Include request/response examples
  - [ ] Document error codes
  - [ ] Create API reference guide

- [ ] **Implementation Guide**
  - [ ] Document setup procedure
  - [ ] Create configuration guide
  - [ ] Document database schema
  - [ ] Create troubleshooting guide
  - [ ] Document maintenance procedures

- [ ] **Authentication Guide**
  - [ ] Document API key management
  - [ ] Document authentication flow
  - [ ] Create security best practices
  - [ ] Document compliance measures

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
- [ ] Input validation on all endpoints
- [ ] API key encryption and rotation
- [ ] Rate limiting per user
- [ ] HTTPS/TLS everywhere
- [ ] SQL injection prevention
- [ ] Prompt injection prevention
- [ ] CORS properly configured
- [ ] Logging of all security events

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

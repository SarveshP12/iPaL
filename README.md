# ICICI Bank iPaL - Intelligent Personal Assistant Layer

Welcome to the ICICI Bank iPaL project repository. This project implements an intelligent RAG (Retrieval-Augmented Generation) Chatbot system designed to enhance customer service and user experience.

## 📋 Project Overview

iPaL (Intelligent Personal Assistant Layer) is a cutting-edge conversational AI solution that leverages RAG technology to provide accurate, context-aware responses to user queries. The system combines the power of large language models with domain-specific knowledge retrieval to deliver superior customer interactions.

## 📚 Essential Documentation

Before diving into the codebase, please review these comprehensive documents to understand the project thoroughly:

### 🗺️ Project Execution Roadmap
For phase-wise implementation planning, refer to the detailed folder:
- **[Execution Phases Directory](./execution_phases/README.md)**

This directory divides the full project into practical execution phases with clear deliverables and exit criteria.

### 1. 📄 [ICICIBank-PRD.pdf](./ICICIBank-PRD.pdf)
**Product Requirements Document**

This document is your starting point for understanding the project. It contains:
- **Business Objectives**: Why we're building iPaL and what problems it solves
- **Stakeholder Requirements**: Expectations from various business units
- **User Stories & Use Cases**: Detailed scenarios of how users will interact with the system
- **Feature Specifications**: Complete list of features with priorities
- **Success Criteria**: Metrics and KPIs to measure project success
- **Scope & Constraints**: What's included and what's not in this release

**🎯 Read this if you want to understand:** What we're building and why

---

### 2. 🎨 [ICICIBank-DesignDoc.pdf](./ICICIBank-DesignDoc.pdf)
**Design Document**

This document provides the blueprint for the entire system:
- **System Architecture**: High-level and detailed architectural diagrams
- **Component Design**: Individual component specifications and interactions
- **Data Models**: Database schemas and data flow diagrams
- **API Specifications**: REST/GraphQL endpoints and contracts
- **UI/UX Design**: Interface mockups, user flows, and design patterns
- **Security Design**: Authentication, authorization, and data protection mechanisms
- **Integration Points**: How different services communicate

**🎯 Read this if you want to understand:** How the system is architected and designed

---

### 3. ⚙️ [Technical_Stack_Document_RAG_Chatbot.pdf](./Technical_Stack_Document_RAG_Chatbot.pdf)
**Technical Stack & Implementation Guide**

This document covers the technical implementation details:
- **Technology Stack**: Complete list of frameworks, libraries, and tools
- **RAG Implementation**: Vector databases, embedding models, and retrieval strategies
- **Backend Technologies**: Server frameworks, APIs, and middleware
- **Frontend Technologies**: UI frameworks, state management, and component libraries
- **Infrastructure**: Cloud services, deployment strategies, and CI/CD pipelines
- **Development Setup**: Environment configuration and local development guidelines
- **Best Practices**: Coding standards, testing strategies, and performance optimization

**🎯 Read this if you want to understand:** What technologies we're using and how to implement features

---

## 🏗️ Repository Structure

```
iPaL/
├── README.md                                      # This file
├── ICICIBank-PRD.pdf                             # Product Requirements
├── ICICIBank-DesignDoc.pdf                       # Design Specifications
├── Technical_Stack_Document_RAG_Chatbot.pdf      # Technical Stack Guide
│
└── frontend/                                      # Next.js Frontend Application
    ├── README.md                                  # Frontend-specific documentation
    ├── src/                                       # Source code
    ├── public/                                    # Static assets
    └── package.json                               # Dependencies
```

## 🚀 Quick Start Guide

### For New Team Members

1. **Read the Documentation** (Recommended Order):
   - Start with `ICICIBank-PRD.pdf` for business context
   - Review `ICICIBank-DesignDoc.pdf` for system architecture
   - Study `Technical_Stack_Document_RAG_Chatbot.pdf` for implementation details

2. **Set Up Your Environment**:
   ```bash
   # Navigate to frontend
   cd frontend
   
   # Install dependencies
   npm install
   
   # Start development server
   npm run dev
   ```

3. **Access the Application**:
   - Frontend: http://localhost:3000

### For Developers

- See [frontend/README.md](./frontend/README.md) for detailed frontend setup and development instructions
- Refer to the Technical Stack Document for coding standards and best practices
- Check the Design Document for API specifications and integration guidelines

### For Project Managers

- Review the PRD for feature roadmap and priorities
- Check success metrics defined in the PRD
- Refer to the Design Document for technical feasibility and timelines

### For Designers

- Consult the Design Document for UI/UX guidelines
- Reference the PRD for user personas and user journeys
- Follow the design system specifications outlined in the documentation

## 🛠️ Technology Highlights

- **Frontend**: Next.js 16, React 19, TypeScript, Tailwind CSS
- **AI/ML**: RAG (Retrieval-Augmented Generation) Architecture
- **Modern Stack**: Server-side rendering, API routes, optimized performance

## 📞 Support & Communication

For questions or clarifications:
- **Technical Issues**: Refer to Technical Stack Document
- **Feature Questions**: Check the PRD
- **Design Queries**: Review the Design Document

## 📝 Important Notes

⚠️ **Before Starting Development**:
- Ensure you've read all three documentation PDFs
- Understand the project requirements and constraints
- Familiarize yourself with the technical stack
- Follow the coding standards and conventions specified in the Technical Stack Document

✅ **Development Best Practices**:
- Always refer to the Design Document for implementation consistency
- Validate features against PRD requirements
- Follow the architectural patterns defined in the documentation
- Write maintainable, well-documented code

## 🔄 Documentation Updates

These PDF documents are the source of truth for the project. If you notice any discrepancies between the code and documentation, please:
1. Verify the latest version of the PDFs
2. Raise the issue with the project lead
3. Update implementation to match approved documentation

---

**Last Updated**: February 2026  
**Project**: ICICI Bank iPaL - RAG Chatbot  
**Status**: Active Development

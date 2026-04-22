# ICICI Bank iPaL - RAG Chatbot Frontend

This is the frontend application for ICICI Bank's iPaL (Intelligent Personal Assistant Layer) project, featuring a RAG (Retrieval-Augmented Generation) Chatbot built with [Next.js](https://nextjs.org).

## 📚 Documentation

For comprehensive project understanding, please refer to the following documents located in the root directory:

### 1. [Product Requirements Document (PRD)](../ICICIBank-PRD.pdf)
The PRD outlines the business requirements, objectives, user stories, and functional specifications for the iPaL project. This document provides insights into:
- Project objectives and scope
- User personas and use cases
- Feature requirements and prioritization
- Success metrics and KPIs

### 2. [Design Document](../ICICIBank-DesignDoc.pdf)
The Design Document provides detailed architectural and design specifications including:
- System architecture and design patterns
- Component structure and relationships
- UI/UX design guidelines
- Data flow and state management
- API integration specifications

### 3. [Technical Stack Document](../Technical_Stack_Document_RAG_Chatbot.pdf)
This document covers the complete technical stack and implementation details:
- Technology choices and justifications
- RAG chatbot implementation approach
- Backend and frontend technology stack
- Development and deployment infrastructure
- Integration points and dependencies

## 🛠️ Tech Stack

- **Framework:** Next.js 16.1.6 (App Router)
- **UI Library:** React 19.2.3
- **Language:** TypeScript 5
- **Styling:** Tailwind CSS 4
- **Linting:** ESLint with Next.js configuration

## 🚀 Getting Started

### Prerequisites

- Node.js 20+ installed
- npm, yarn, pnpm, or bun package manager

### Installation

1. Clone the repository
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

3. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   # or
   pnpm install
   ```

### Development Server

Run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the application.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

### Build for Production

```bash
npm run build
npm run start
```

### Code Quality

Run linting:

```bash
npm run lint
```

## 📁 Project Structure

```
frontend/
├── src/
│   └── app/
│       ├── globals.css      # Global styles
│       ├── layout.tsx        # Root layout component
│       └── page.tsx          # Home page
├── public/                   # Static assets
├── eslint.config.mjs        # ESLint configuration
├── next.config.ts           # Next.js configuration
├── tailwind.config.js       # Tailwind CSS configuration
├── tsconfig.json            # TypeScript configuration
└── package.json             # Dependencies and scripts
```

## 🔗 Additional Resources

### Next.js Resources

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial
- [Next.js GitHub repository](https://github.com/vercel/next.js)

### Fonts

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## 🚢 Deployment

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out the [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

## 📝 Notes

- Ensure you've reviewed all three documentation PDFs before starting development
- Follow the design guidelines specified in the Design Document
- Refer to the Technical Stack Document for implementation best practices
- Check the PRD for feature requirements and acceptance criteria

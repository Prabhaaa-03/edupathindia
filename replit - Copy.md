# EduPath India - Educational Platform

## Overview

EduPath India is a comprehensive educational platform designed specifically for Indian students, providing an all-in-one solution for career preparation and academic success. The platform offers exam notifications, AI-powered mock interviews, resume building tools, skill challenges, and multilingual support across Hindi, Telugu, Tamil, Bengali, and English.

The application serves as a centralized hub that reduces information overload by aggregating educational opportunities and providing personalized guidance through AI-enhanced features. It targets students preparing for various competitive exams, job applications, and career development.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: React with TypeScript and Vite for fast development and optimal builds
- **Styling**: Tailwind CSS with shadcn/ui component library for consistent, accessible UI components
- **State Management**: TanStack Query for server state management and caching
- **Routing**: Wouter for lightweight client-side routing
- **Design System**: Custom design tokens with dark/light theme support via CSS variables

### Backend Architecture  
- **Runtime**: Node.js with Express server
- **Language**: TypeScript with ES modules for type safety and modern JavaScript features
- **API Design**: RESTful API with structured JSON responses and comprehensive error handling
- **Session Management**: Express sessions with PostgreSQL session store
- **Middleware**: Custom logging, CORS handling, and request/response interceptors

### Data Storage Solutions
- **Primary Database**: PostgreSQL with Neon serverless hosting
- **ORM**: Drizzle ORM for type-safe database operations and migrations
- **Schema**: Comprehensive relational schema including users, notifications, interview sessions, skill challenges, and progress tracking
- **Storage Strategy**: In-memory fallback storage for development with production PostgreSQL deployment

### Authentication and Authorization
- **Session-based Authentication**: Traditional session cookies with PostgreSQL session persistence
- **User Management**: Complete user lifecycle with profile customization and language preferences
- **Security**: Password hashing, session management, and secure cookie handling

### External Dependencies

#### AI Services
- **Google Gemini AI**: Powers mock interview question generation, response analysis, and personalized feedback systems
- **Translation Services**: Multi-language content delivery supporting Hindi, Telugu, Tamil, Bengali, and English

#### UI and Styling
- **Radix UI**: Accessible, unstyled UI primitives for complex components like dropdowns, dialogs, and form controls
- **Tailwind CSS**: Utility-first CSS framework with custom design tokens
- **shadcn/ui**: Pre-built component library built on Radix UI with consistent styling
- **Lucide React**: Icon library for consistent iconography

#### Fonts and Typography
- **Google Fonts**: Inter for Latin text and Noto Sans family for Indian language support
- **Font Loading**: Optimized font loading with preconnect and display swap strategies

#### Development Tools
- **Vite**: Modern build tool with HMR and optimized production builds
- **Replit Integration**: Development environment integration with cartographer and error overlay plugins
- **ESBuild**: Fast bundling for server-side code compilation

#### Data Validation
- **Zod**: Runtime type validation for API requests and database schema validation
- **React Hook Form**: Form state management with validation integration

#### Utility Libraries
- **date-fns**: Date manipulation and formatting for deadline calculations
- **clsx/tailwind-merge**: Conditional class name utilities for dynamic styling
- **nanoid**: Secure unique ID generation for database records

The architecture emphasizes type safety, developer experience, and scalability while maintaining focus on the Indian educational market's specific needs including multilingual support and culturally relevant features.
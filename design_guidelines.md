# Design Guidelines: EduPath India - Educational Platform

## Design Approach
**Reference-Based Approach**: Drawing inspiration from modern educational platforms like Coursera and Khan Academy, combined with the clean, mobile-first design patterns of successful Indian apps like BYJU'S and Unacademy. The design prioritizes accessibility, multilingual support, and mobile-first usage patterns common among Indian students.

## Core Design Elements

### A. Color Palette
**Primary Colors:**
- Light Mode: 220 85% 25% (Deep education blue)
- Dark Mode: 220 80% 15% (Darker education blue)

**Secondary Colors:**
- Success/Progress: 142 70% 45% (Educational green)
- Warning/Deadlines: 25 85% 55% (Alert orange)
- Background variations: 220 20% 98% (light), 220 25% 8% (dark)

### B. Typography
**Font Families:**
- Primary: Inter (via Google Fonts CDN)
- Regional Languages: Noto Sans (supports Hindi, Telugu, Tamil, Bengali)

**Hierarchy:**
- Headlines: font-bold text-2xl to text-4xl
- Body: font-normal text-base
- Captions: font-medium text-sm

### C. Layout System
**Spacing Units:** Consistent use of Tailwind units 2, 4, 6, and 8
- Component padding: p-4, p-6
- Section margins: mb-6, mb-8
- Grid gaps: gap-4, gap-6

### D. Component Library

**Navigation:**
- Bottom tab navigation for mobile (primary)
- Sidebar for desktop with collapsible sections
- Language switcher prominently placed in header

**Core Components:**
- Notification cards with priority indicators (color-coded borders)
- Progress tracking rings and bars
- Interactive quiz/challenge cards
- Resume builder step indicators
- Mock interview chat interface
- Application tracker timeline

**Data Displays:**
- Dashboard widgets with rounded corners (rounded-lg)
- Exam countdown timers with urgency states
- Skill progress charts using simple bar visualizations
- Career pathway flowcharts

**Forms:**
- Multi-step forms with clear progress indicators
- Regional language input support
- File upload areas for documents
- Smart form validation with helpful error messages

**Overlays:**
- Modal dialogs for detailed exam information
- Notification permission prompts
- Language selection overlay
- Mock interview feedback screens

### E. Key Design Principles

**Mobile-First Approach:**
- Touch-friendly button sizes (min-h-12)
- Thumb-friendly navigation zones
- Readable text sizes on small screens
- Efficient use of vertical space

**Multilingual Considerations:**
- Flexible layouts accommodating text expansion
- Right-to-left reading support where needed
- Clear language indicators throughout interface
- Consistent iconography across languages

**Accessibility & Inclusion:**
- High contrast ratios for text readability
- Screen reader friendly navigation
- Keyboard navigation support
- Consistent focus states using ring utilities

**Information Hierarchy:**
- Clear visual distinction between urgent and regular notifications
- Prominent placement of deadlines and important dates
- Progressive disclosure for complex information
- Scannable content layouts with clear headings

## Images
**Hero Section:** Large, inspiring image of diverse Indian students studying/celebrating success (approximately 60% viewport height on desktop, 40% on mobile)

**Feature Illustrations:** Simple, modern illustrations showing:
- Students receiving notifications on phones
- Mock interview scenarios
- Resume building process
- Skill development activities

**Placement:** Hero image in landing section, feature illustrations integrated within content sections, user avatar placeholders in profile areas.
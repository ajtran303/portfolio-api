# Portfolio UI

## Summary

React frontend for my developer portfolio, fetching Markdown-based projects from a GraphQL API. Built async and type-safe with **TypeScript**, with tests written using **Vitest** and **Testing Library**. Features smooth UI/UX, scroll animations, an interactive projects carousel, and a **dynamic, visually rich interface** using Vanta.NET backgrounds and translucent card layouts.

[View the code](https://github.com/ajtran303/portfolio-ui)

---

## Highlights

- **Hero Section:** Animated with smooth transitions and call-to-action button
- **About Section:** Casual summary of skills and tech stack, enhanced with:
    - **Interactive Vanta.NET background** (gold lines + nodes)
    - **Translucent "glass card"** overlay
    - **Gold-to-blue gradient wrapper** behind the card
    - Smooth fade-in animation on scroll
- **Projects Carousel:** Clickable carousel of projects that **scrolls to the top of the section** when navigating between projects
    - Each project includes an **inner image carousel** for project screenshots
    - Images are automatically removed from the markdown content and displayed in the carousel
    - Carousel is responsive and mobile-friendly, with navigation buttons and index counter
- **Responsive Design:** Mobile-friendly with smooth transitions
- **Scroll Animations:** About section fades in as you scroll
- **React Hooks Used:** `useState`, `useRef`, and `useEffect` for animations, Vanta.NET initialization, and intersection observer functionality
- **Type-safe & Tested:** TypeScript types, Vitest, and Testing Library

---

## Tech Stack

- React  
- TypeScript  
- CSS Modules  
- Vanta.NET & Three.js for dynamic backgrounds  

---

## Demo

- **Live Demo:** [AJ Tran Portfolio](https://ajtran-dev.onrender.com)

---

## Screenshots

![Hero Page Mobile View](/assets/portfolio-ui/hero_page.png)

![About Page Mobile View](/assets/portfolio-ui/about_page.png)

![Project Page Mobile View](/assets/portfolio-ui/project_page.png)

![Project Carousel with Inner Image Carousel](/assets/portfolio-ui/project_carousel.png)

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

- **Live Demo:** [AJ Tran Portfolio](https://ajtran-dev.onrender.com) (Congratulations, you're here!)

---

## Screenshots

![Hero Page Mobile View](https://private-user-images.githubusercontent.com/31839316/528915951-9497bf5e-9788-4bf5-bd22-97436b8f2033.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjYyNzg3NzcsIm5iZiI6MTc2NjI3ODQ3NywicGF0aCI6Ii8zMTgzOTMxNi81Mjg5MTU5NTEtOTQ5N2JmNWUtOTc4OC00YmY1LWJkMjItOTc0MzZiOGYyMDMzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjIxVDAwNTQzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVmYTQ3Nzc0MmMxOTBiNDM1MDIxZGQxMzJhMWU2ZGExYzE0YmU0ZmYyMGY1NDZlYTIzNzZhOGE4NGViYzZlZWUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.1IeVdfDljD2TvnERqFVkRpiuxH1WvEJ31CLX1RfuA2w)

![About Page Mobile View](https://private-user-images.githubusercontent.com/31839316/528916009-7dc546c9-a597-4cdb-9ab6-ef80980a2eca.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjYyNzg3NzcsIm5iZiI6MTc2NjI3ODQ3NywicGF0aCI6Ii8zMTgzOTMxNi81Mjg5MTYwMDktN2RjNTQ2YzktYTU5Ny00Y2RiLTlhYjYtZWY4MDk4MGEyZWNhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjIxVDAwNTQzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWI0Y2Q5YTU3NzI4YjIwNzg2ZjBkNjUxZGY0NDZiOTBhZTcwZDU3YzhiZjBmYTYyMWQ0Y2EwNGE0YzNhOTg3NjkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.27uH6W3XAXa_MykO20PRdXQlh4G1Tcut9XFB4YWiun8)

![Project Page Mobile View](https://private-user-images.githubusercontent.com/31839316/528916052-06f2a158-738a-4a06-94b5-50bf5ccd9ce8.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjYyNzg3NzcsIm5iZiI6MTc2NjI3ODQ3NywicGF0aCI6Ii8zMTgzOTMxNi81Mjg5MTYwNTItMDZmMmExNTgtNzM4YS00YTA2LTk0YjUtNTBiZjVjY2Q5Y2U4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjIxVDAwNTQzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU3YTQ5MjE2ODc0ZDMxOWYwNjRkZmI3N2Q3ZDJjY2NhOGJlNDQ0MThhNTY1OWNhYjQyNTRlYWRmZjM2NTVkNmUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.5ltg1KVGKmy9dzscj-fJ08cIAi5trvuCwnzJSVQ0tZM)

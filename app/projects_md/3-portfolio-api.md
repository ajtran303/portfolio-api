# Portfolio API

## Summary

A lightweight FastAPI backend serving project data stored as Markdown files. Features async GraphQL endpoints with Strawberry, TDD, and file-based storage. Demonstrates modern Python backend practices for a personal portfolio.

[View the code](https://github.com/ajtran303/portfolio-api/)

---

## Highlights

- **GraphQL API:** Query projects by slug or list all projects
- **Async endpoints:** FastAPI + httpx for asynchronous requests and testing
- **Markdown-powered content:** Projects stored in Markdown and served as HTML
- **Test-Driven Development:** Async tests using pytest and pytest-asyncio
- **Database-free:** Portable and lightweight, no database required

---

## Tech Stack

- Python 3.9+
- FastAPI & Strawberry GraphQL
- `httpx` for async HTTP requests
- Markdown for project content
- Pytest & pytest-asyncio
- Deployment-ready on Render

---

## Demo

- **Live Demo:** [GraphiQL Interface](https://aj-tran-dev-portfolio-api.onrender.com/graphql)

---

## Screenshots

![Portfolio GraphQL API Get All Project Slugs Query](https://private-user-images.githubusercontent.com/31839316/528914794-a1da10c9-4354-43de-aea5-53a1b5d7c2fd.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjYyNzc5NDUsIm5iZiI6MTc2NjI3NzY0NSwicGF0aCI6Ii8zMTgzOTMxNi81Mjg5MTQ3OTQtYTFkYTEwYzktNDM1NC00M2RlLWFlYTUtNTNhMWI1ZDdjMmZkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjIxVDAwNDA0NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPThlYThhOGY1ZWJlMzcyNDUyNDQ1MGQ0MmFiMjczMDA2ZWM4NWIxYzFiYmEzMDQxOTMxZDc5NDViMzMxYWI3OTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.8I11JaNbdyISvwdG7014W_mSjJl4tcu9aCkRhh32t34)

![Portfolio GraphQL API Get Project Content By Slug Query](https://private-user-images.githubusercontent.com/31839316/528915646-1d3afb05-c77c-4a91-8a13-9c3fdeb0bbf0.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjYyNzgxMjUsIm5iZiI6MTc2NjI3NzgyNSwicGF0aCI6Ii8zMTgzOTMxNi81Mjg5MTU2NDYtMWQzYWZiMDUtYzc3Yy00YTkxLThhMTMtOWMzZmRlYjBiYmYwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjIxVDAwNDM0NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVkOWNkNWY5MTBlMWQzMjZmNTYwZTY4YjNhMzMyYjVjNzU0MzUyNWRiZjY5YWE3ZmU0MDFlYzRhMTVhMjlmZTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.9vejEZpk9PKP73DQ9TA57PzteVLhgI9W6QRVJXoBGm8)

![Portfolio GraphQL API Get All Projects Query](https://private-user-images.githubusercontent.com/31839316/528915052-e8511caf-4638-4614-9bf9-489c1b8577da.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjYyNzc5NDUsIm5iZiI6MTc2NjI3NzY0NSwicGF0aCI6Ii8zMTgzOTMxNi81Mjg5MTUwNTItZTg1MTFjYWYtNDYzOC00NjE0LTliZjktNDg5YzFiODU3N2RhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjIxVDAwNDA0NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTAxMzI4OGMwYTdkMzJhOTI5NjE2Nzk3YmRhNTkwNjQzN2Y2YzdhMzE5OTIxNDFlNGFmYTkxZjg4OTFmZjZmMmImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.fC5yWOMImvhlqhpEO1YNV5iZ5qt29Sd0BJboML81MZQ)

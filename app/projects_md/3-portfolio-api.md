# Portfolio API

## Summary

A lightweight **FastAPI backend** serving project data stored as Markdown files. Provides **async GraphQL endpoints** with Strawberry, TDD-tested routes, and file-based storage. Demonstrates modern Python backend practices for a personal portfolio, including async operations, Markdown rendering, and lightweight architecture.

[View the code](https://github.com/ajtran303/portfolio-api/)

---

## Highlights

- **GraphQL API:** Query projects by slug or fetch all projects
- **Async Endpoints:** FastAPI + httpx for asynchronous requests and testing
- **Markdown-powered content:** Projects stored as Markdown, served as HTML
- **Database-free:** File-based storage for a portable and lightweight solution
- **Test-Driven Development:** Async tests using pytest and pytest-asyncio to: fetch existing projects by slug, list all projects, handle empty project directories, and async GraphQL API response validation
- **CORS & Asset Handling:** Static file serving with dynamic ASSETS_BASE_URL
- **Schema-driven:** Strawberry GraphQL types for strong typing and auto-generated IDE

---

## Tech Stack

- Python 3.11+
- FastAPI & Strawberry GraphQL
- `httpx` for async HTTP requests and testing
- Markdown for project content rendering
- Pytest & pytest-asyncio for TDD
- Deployment-ready on Render

---

## Architecture

**Backend**
- FastAPI application with modular routers
- Strawberry GraphQL for schema-driven endpoints
- Markdown file parsing and HTML conversion
- Static file serving for project assets

**Testing**
- Async test suite using pytest-asyncio and httpx ASGI transport
- Tests include project retrieval by slug, listing all projects, and empty state handling

**Middleware**
- CORS enabled for cross-origin requests
- StaticFiles serving project assets under `/assets`

---

- **Live Demo:** [GraphiQL Interface](https://aj-tran-dev-portfolio-api.onrender.com/graphql)

---

## Screenshots

![Portfolio GraphQL API Get All Project Slugs Query](/assets/portfolio-api/get_all_slugs.png)

![Portfolio GraphQL API Get Project Content By Slug Query](/assets/portfolio-api/get_project_content.png)

![Portfolio GraphQL API Get All Projects Query](/assets/portfolio-api/get_all_projects.png)

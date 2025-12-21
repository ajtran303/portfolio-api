# Portfolio API

## Summary

A lightweight **FastAPI backend** serving project data stored as Markdown files. Provides **async GraphQL endpoints** with Strawberry, TDD-tested routes, and file-based storage. Demonstrates modern Python backend practices for a personal portfolio, including async operations, Markdown rendering, and lightweight architecture.

[View the code on GitHub](https://github.com/ajtran303/portfolio-api/)

---

## Highlights

- **GraphQL API:** Query projects by slug or fetch all projects
- **Async Endpoints:** FastAPI + httpx for asynchronous requests and testing
- **Markdown-powered content:** Projects stored as Markdown, served as HTML
- **Database-free:** File-based storage for a portable and lightweight solution
- **Test-Driven Development:** Async tests using pytest and pytest-asyncio to: fetch existing projects by slug, list all projects, handle empty project directories, and async GraphQL API response validation
- **CORS & Asset Handling:** CORS enabled for cross-origin requests and StaticFiles serving project assets under `/assets`
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

- **Live Demo:** [GraphiQL Interface](https://aj-tran-dev-portfolio-api.onrender.com/graphql)

---

## Screenshots

![Portfolio GraphQL API Get All Project Slugs Query](/assets/portfolio-api/get_all_slugs.png)

![Portfolio GraphQL API Get Project Content By Slug Query](/assets/portfolio-api/get_project_content.png)

![Portfolio GraphQL API Get All Projects Query](/assets/portfolio-api/get_all_projects.png)

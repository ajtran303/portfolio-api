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

![Portfolio GraphQL API Get All Project Slugs Query](/assets/portfolio-api/get_all_slugs.png)

![Portfolio GraphQL API Get Project Content By Slug Query](/assets/portfolio-api/get_project_content.png)

![Portfolio GraphQL API Get All Projects Query](/assets/portfolio-api/get_all_projects.png)

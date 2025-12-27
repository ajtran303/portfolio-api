# Portfolio API

## Summary

FastAPI backend serving portfolio projects via GraphQL. Reads Markdown files from disk, converts to HTML, and serves through async Strawberry GraphQL endpoints. No database required. Portable, lightweight, and fully tested with pytest.

[View the code on GitHub](https://github.com/ajtran303/portfolio-api/)

---

## Highlights

- **GraphQL API:** Query single project by slug or fetch all projects
- **Markdown to HTML:** File-based content storage with automatic HTML rendering
- **Async Architecture:** FastAPI + Strawberry for non-blocking request handling
- **Static Asset Serving:** Images served via `/assets` with URL rewriting in rendered content
- **Test-Driven:** Async tests with pytest-asyncio covering queries, edge cases, and empty states

---

## Tech Stack

- Python 3.11+
- FastAPI + Strawberry GraphQL
- Markdown for content rendering
- pytest + pytest-asyncio
- Deployed on Render

---

## Live Demo

[GraphiQL Interface](https://aj-tran-dev-portfolio-api.onrender.com/graphql)

---

## Screenshots

![Portfolio GraphQL API Get All Project Slugs Query](/assets/portfolio-api/get_all_slugs.png)

![Portfolio GraphQL API Get Project Content By Slug Query](/assets/portfolio-api/get_project_content.png)

![Portfolio GraphQL API Get All Projects Query](/assets/portfolio-api/get_all_projects.png)

# Portfolio API

## Summary

A lightweight FastAPI backend serving project data stored as Markdown files. Features async GraphQL endpoints with Strawberry, TDD, and file-based storage—demonstrating modern Python backend practices for a personal portfolio.

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
- httpx for async HTTP requests
- Markdown for project content
- Pytest & pytest-asyncio
- Deployment-ready on Render

---

## Demo

- **Live Demo:** [GraphiQL Interface](https://aj-tran-dev-portfolio-api.onrender.com/graphql)

### Example Queries

1. Get a single project by slug

```graphql
query GetProject($slug: String!) {
  project(slug: $slug) {
    slug
    content
  }
}
```

Example Variables:

```json
{
  "slug": "learnforge-lms"
}
```

```json
{
  "slug": "portfolio-api"
}
```

Example Response:
{
  "data": {
    "project": {
      "slug": "portfolio-api",
      "content": "<h1>Portfolio API</h1><p>Description here...</p>"
    }
  }
}


2. List all projects

```graphql
query {
  allProjects {
    slug
    content
  }
}
```

Example Response

```json
{
  "data": {
    "allProjects": [
      {
        "slug": "learnforge-lms",
        "content": "<h1>LearnForge LMS</h1><p>Project description...</p>"
      },
      {
        "slug": "portfolio-api",
        "content": "<h1>Portfolio API</h1><p>Project description...</p>"
      }
    ]
  }
}
```

<!-- - **Demo Video:** [Watch on YouTube]() *(TODO: Record demo)* -->
<!--  -->
<!-- --- -->
<!--  -->
<!-- ## Screenshots -->

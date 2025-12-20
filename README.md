# Portfolio API

A personal GraphQL API for serving project descriptions from Markdown files.

## Features

- FastAPI + Strawberry GraphQL
- Project content sourced from Markdown files
- GraphQL IDE (GraphiQL) included for easy testing
- Async support for high performance

## Setup

1. Clone the repository:

```bash
git clone git@github.com:ajtran303/portfolio-api.git
cd portfolio-api
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the API:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000/graphql.

## Testing

Run tests using pytest:

```bash
pytest -v
```

## Example GraphQL Queries

### Get a project by slug:

```graphql
query GetProject($slug: String!) {
  project(slug: $slug) {
    slug
    content
  }
}
```

### List all projects:

```graphql
query GetAllProjects {
  allProjects {
    slug
    content
  }
}


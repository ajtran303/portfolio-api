import pytest
from httpx import AsyncClient, ASGITransport
from pathlib import Path
from app.main import app

PROJECTS_DIR = Path(__file__).parent.parent / "app" / "projects_md"

@pytest.mark.asyncio
async def test_get_existing_project():
    test_file = PROJECTS_DIR / "test_project.md"
    test_content = "# Test Project\nThis is a test project."
    PROJECTS_DIR.mkdir(exist_ok=True)
    test_file.write_text(test_content, encoding="utf-8")

    
    query = """
    query GetProject($slug: String!) {
        project(slug: $slug) {
            slug
            content
        }
    }
    """

    variables = {"slug": "test_project"}

    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("/graphql", json={"query": query, "variables": variables})

    assert response.status_code == 200
    data = response.json()["data"]["project"]
    assert data["slug"] == "test_project"
    assert "<h1>Test Project</h1>" in data["content"]
    assert "<p>This is a test project.</p>" in data["content"]

    test_file.unlink()

@pytest.mark.asyncio
async def test_get_nonexistent_project():
    query = """
    query GetProject($slug: String!) {
        project(slug: $slug) {
          slug
          content
        }
    }
    """
    variables = {"slug": "no_such_project"}

    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("/graphql", json={"query": query,  "variables": variables})

    assert response.status_code == 200
    data = response.json()["data"]["project"]
    assert data is None

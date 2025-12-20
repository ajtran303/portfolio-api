from typing import AsyncGenerator, Generator, Callable
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from pathlib import Path
from app.main import app

PROJECTS_DIR = Path(__file__).parent.parent / "app" / "projects_md"

@pytest.fixture
def project_file() -> Generator[Callable[[str, str], Path], None, None]:
    created_files = []

    def _create(filename: str, content: str):
        PROJECTS_DIR.mkdir(exist_ok=True)
        path = PROJECTS_DIR / filename
        path.write_text(content, encoding="utf-8")
        created_files.append(path)
        return path

    yield _create

    for path in created_files:
        if path.exists():
            path.unlink

@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:\
        yield ac

@pytest.mark.asyncio
async def test_get_existing_project(client: AsyncClient, project_file: Callable):
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

    response = await client.post("/graphql", json={"query": query, "variables": variables})

    assert response.status_code == 200
    data = response.json()["data"]["project"]
    assert data["slug"] == "test_project"
    assert "<h1>Test Project</h1>" in data["content"]
    assert "<p>This is a test project.</p>" in data["content"]

    test_file.unlink()

@pytest.mark.asyncio
async def test_get_nonexistent_project(client: AsyncClient):
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

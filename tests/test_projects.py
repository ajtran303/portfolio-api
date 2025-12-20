from typing import AsyncGenerator, Generator, Callable
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from pathlib import Path
from app.main import app


@pytest.fixture
def project_file(temp_projects_dir: Path) -> Generator[Callable[[str, str], Path], None, None]:

    def _create(filename: str, content: str):
        path = temp_projects_dir / filename
        path.write_text(content, encoding="utf-8")
        return path

    yield _create


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_get_existing_project(client: AsyncClient, project_file: Callable):
    project_file("test_project.md", "# Test Project\nThis is a test project.")
    
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

    response = await client.post("/graphql", json={"query": query,  "variables": variables})

    assert response.status_code == 200
    data = response.json()["data"]["project"]
    assert data is None


@pytest.mark.asyncio
async def test_list_all_projects(client: AsyncClient, project_file):
    project_file("project1.md", "# Project 1\nContent 1")
    project_file("project2.md", "# Project 2\nContent 2")

    query = """
    query GetAllProjects {
        allProjects {
            slug
            content
        }
    }
    """

    response = await client.post("/graphql", json={"query": query})
    assert response.status_code == 200

    projects = response.json()["data"]["allProjects"]
    slugs = [project["slug"] for project in projects]
    assert "project1" in slugs
    assert "project2" in slugs

    contents = [project["content"] for project in projects]
    assert any("Project 1" in c for c in contents)
    assert any("Project 2" in c for c in contents)


@pytest.mark.asyncio
async def test_list_all_projects_empty(client: AsyncClient, temp_projects_dir):
    query = """
    query GetAllProjects {
        allProjects {
            slug
            content
        }
    }
    """

    response = await client.post("/graphql", json={"query": query})
    assert response.status_code == 200

    data = response.json()["data"]["allProjects"]
    assert isinstance(data, list)
    assert len(data) == 0

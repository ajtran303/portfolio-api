from app import config
from app.config import settings

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import markdown
from pathlib import Path
from typing import Optional

import strawberry
from strawberry.fastapi import GraphQLRouter


BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "app" / "projects_md" / "assets"


app = FastAPI()


if not settings.ASSETS_BASE_URL:
    raise RuntimeError("ASSETS_BASE_URL must be set")


app.mount(
    "/assets",
    StaticFiles(directory=ASSETS_DIR),
    name="assets",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def render_markdown(md: str) -> str:
    """
    Convert Markdown to HTML and rewrite asset URLs
    so images load from the backend origin.
    """
    html = markdown.markdown(md)
    return html.replace(
        'src="/assets/',
        f'src="{settings.ASSETS_BASE_URL}/'
    )


@strawberry.type
class Project:
    slug: str
    content: str


@strawberry.type
class Query:
    @strawberry.field
    def project(self, slug: str) -> Optional[Project]:
        md_file = config.PROJECTS_DIR / f"{slug}.md"
        if not md_file.exists():
            return None

        content = md_file.read_text(encoding="utf-8")
        html_content = render_markdown(content)

        return Project(slug=slug, content=html_content)

    @strawberry.field(name="allProjects")
    def all_projects(self) -> list[Project]:
        projects: list[Project] = []

        for md_file in config.PROJECTS_DIR.glob("*.md"):
            slug = md_file.stem
            content = md_file.read_text(encoding="utf-8")
            html_content = render_markdown(content)

            projects.append(Project(slug=slug, content=html_content))

        return projects


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema, graphql_ide="graphiql")

app.include_router(graphql_app, prefix="/graphql")

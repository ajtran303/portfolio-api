from app import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import markdown
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import Optional


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
        content = md_file.read_text(encoding='utf-8')
        html_content = markdown.markdown(content)
        return Project(slug=slug, content=html_content)

    @strawberry.field(name="allProjects")
    def all_projects(self) -> list[Project]:
        projects = []
        for md_file in config.PROJECTS_DIR.glob("*md"):
            slug = md_file.stem
            content = md_file.read_text(encoding="utf-8")
            html_content = markdown.markdown(content)
            projects.append(Project(slug=slug, content=html_content))
        return projects


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema, graphql_ide="graphiql")
app.include_router(graphql_app, prefix="/graphql")

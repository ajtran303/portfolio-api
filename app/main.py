from fastapi import FastAPI
from pathlib import Path
import markdown
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import Optional

app = FastAPI()
PROJECTS_DIR = Path(__file__).parent / "projects_md"

@strawberry.type
class Project:
    slug: str
    content: str

@strawberry.type
class Query:
    @strawberry.field
    def project(self, slug: str) -> Optional[Project]:
        md_file = PROJECTS_DIR / f"{slug}.md"
        if not md_file.exists():
            return None
        content = md_file.read_text(encoding='utf-8')
        html_content = markdown.markdown(content)
        return Project(slug=slug, content=html_content)

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema, graphql_ide="graphiql")
app.include_router(graphql_app, prefix="/graphql")

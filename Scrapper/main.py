
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from Scrapper.Models import Scraper

app=FastAPI()
page=Scraper()

@app.get("/")
async def check_server():
    return  {"msg": "Server running"}

# scrap data by page name
@app.get("/{pageName}",tags=["pages"])
async def get_page_posts_by_page_name(pageName):
    return page.scrapdata(pageName)

# customize OAS metadata
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Facebook scrapper",
        version="0.0.1",
        description="This assessement is  for DataEngineer  job application at ELYADATA",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

tags_metadata = [
    {
        "name": "pages",
        "description": "get page informations (name, followers, posts...) by page name and store data in MongoDB",
    },
]

app.openapi = custom_openapi
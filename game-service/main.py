from fastapi import FastAPI

from routers import api_router

app = FastAPI(title="Chess Capital BAckend")

app.include_router(api_router)

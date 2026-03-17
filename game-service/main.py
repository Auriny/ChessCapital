from fastapi import FastAPI

from exceptions import GameNotFoundError, exc_handler
from routers import api_router
from utils.startup import lifespan

app = FastAPI(
    title="Chess Capital Backend",
    lifespan=lifespan, # type: ignore[arg-type]
    exception_handlers={GameNotFoundError: exc_handler}
)

app.include_router(api_router)

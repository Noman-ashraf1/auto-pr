from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to AutoPR AI"
    }
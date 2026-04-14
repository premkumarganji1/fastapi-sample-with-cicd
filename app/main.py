# app/main.py
from fastapi import FastAPI
from mangum import Mangum
from app.routes.sample_route import router
from app.core.config import settings
from app.utils.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.include_router(router, prefix="/apis")


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# For AWS Lambda
handler = Mangum(app)

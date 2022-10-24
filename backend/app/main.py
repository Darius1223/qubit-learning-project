import structlog
import uvicorn
from fastapi import FastAPI

from app import settings
from app.router import router

app = FastAPI(debug=settings.DEBUG)
app.include_router(router=router)

logger = structlog.get_logger(module="main")


@app.on_event("startup")
def startup_app():
    logger.debug("startup application")


if __name__ == "__main__":
    uvicorn.run(app=app)

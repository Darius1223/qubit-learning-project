from fastapi import APIRouter

from app import settings
from app.services import task_service

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/health_check")
async def health_check():
    return {"message": "Health ok!"}


@router.get("/test_rq")
async def rq_test():
    task_service.create()
    return {"message": "rq is ok"}

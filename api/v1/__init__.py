from fastapi import APIRouter
from .breaches import breaches
v1 = APIRouter()

v1.include_router(router=breaches, prefix="/breaches", tags=["Breaches"])
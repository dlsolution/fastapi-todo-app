from fastapi import APIRouter
from ..v1 import users, items, auth

router = APIRouter(prefix='/v1')
router.include_router(users.router)
router.include_router(items.router)
router.include_router(auth.router)

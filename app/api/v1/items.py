from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import Session
from config.database import get_db
from utils.response import response_item, response_pagination
from app.services import items as service
from utils.utils import authorize, requires
from ..v1.presenters.items import present_list, present_detail
from ..v1.requests.items import CreateItem


router = APIRouter()

@router.post("/users/{user_id}/items")
@requires('authenticated')
@authorize(role=['admin'])
async def create_item_for_user(
    request: Request,
    user_id: int, 
    input_data: CreateItem, 
    db: Session = Depends(get_db)
):
    item = service.create_user_item(db=db, item=input_data, user_id=user_id)
    return response_item(present_detail(item))


@router.get("/items")
@requires('authenticated')
@authorize(role=['admin'])
async def read_items(
    request: Request, 
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    items = service.get_items(db, skip=skip, limit=limit)
    return response_pagination(present_list(items), limit)

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from config.database import get_db
from utils.response import response_item, response_pagination
from app.services import items as service
from ..v1.presenters.items import present_list, present_detail
from ..v1.requests.items import CreateItem


router = APIRouter()


@router.post("/users/{user_id}/items")
def create_item_for_user(
    user_id: int, input_data: CreateItem, db: Session = Depends(get_db)
):
    return response_item(present_detail(service.create_user_item(db=db, item=input_data, user_id=user_id)))


@router.get("/items")
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = service.get_items(db, skip=skip, limit=limit)
    return response_pagination(present_list(items), limit)

from fastapi import Depends, APIRouter, HTTPException, Request
from sqlalchemy.orm import Session
from config.database import get_db
from utils.response import response_item, response_pagination
from app.services import users as service
from ..v1.presenters.users import present_list, present_detail
from ..v1.requests.users import CreateUser
from utils.utils import requires, authorize


router = APIRouter()

@router.post("/users")
async def create_user(
    request: Request, 
    input_data: CreateUser, 
    db: Session = Depends(get_db)
):
    db_user = service.get_user_by_email(db, email=input_data.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return response_item(present_detail(service.create_user(db=db, user=input_data)))


@router.get("/users")
@requires('authenticated')
@authorize(role=['admin'])
async def read_users(
    request: Request, 
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    users = service.get_users(db, skip=skip, limit=limit)
    return response_pagination(present_list(users), limit)


@router.get("/users/{user_id}")
@requires('authenticated')
@authorize(role=['admin'])
async def read_user(
    request: Request, 
    user_id: int, 
    db: Session = Depends(get_db)
):
    db_user = service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return response_item(present_detail(db_user))

from fastapi import Request, status, HTTPException, APIRouter, Depends
from app.services.auth import get_current_user
from utils.response import response_item
from ..v1.requests.users import UserLogin
from sqlalchemy.orm import Session
from config.database import get_db
from app.services import users as usersService
from utils.utils import requires, authorize, verify_password, create_access_token, create_refresh_token


router = APIRouter()

@router.post('/login')
async def login(input_data: UserLogin, db: Session = Depends(get_db)):
    user = usersService.get_user_by_email(db, input_data.email)
    if user is None or not verify_password(input_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    access_token = create_access_token(data={"sub": user.email, "role": user.role})
    refresh_token = create_refresh_token(data={"sub": user.email, "role": user.role})
    return response_item({
        "access_token": access_token, 
        "refresh_token": refresh_token, 
        "token_type": "bearer"
    })

@router.get("/me")
@requires('authenticated')
@authorize(role=['admin'])
async def me(request: Request, db: Session = Depends(get_db)):
    profile = request.user['profile']
    user = get_current_user(db, profile)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Data not found",
        )
    return response_item(user)

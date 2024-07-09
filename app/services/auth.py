from app.models.user import User
from sqlalchemy.orm import Session


def get_current_user(db: Session, email: str) -> object:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return {}

    return {
        "id": user.id,
        "email": user.email,
        "is_active": user.is_active
    }

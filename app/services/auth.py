from app.models.user import User
from sqlalchemy.orm import Session


def get_current_user(db: Session, profile: object) -> object:
    email = profile['email']
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return {}

    return {
        "id": user.id,
        "email": user.email,
        "role": user.role,
        "is_active": user.is_active
    }

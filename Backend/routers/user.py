from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserOut, RoleUpdate

router = APIRouter(prefix="/users", tags=["Users"])


# ---------------- REGISTER USER ----------------
@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    # Email duplicate check
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(
        email=user.email,
        password=user.password,
        role="user"   # ✅ default role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# ---------------- UPDATE ROLE ----------------
@router.put("/{user_id}/role")
def update_role(user_id: int, data: RoleUpdate, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.role = data.role
    db.commit()

    return {
        "message": "Role updated successfully"
    }

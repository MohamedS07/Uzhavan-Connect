from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    password: str
    role: str | None = None   # 👈 VERY IMPORTANT

class UserOut(UserCreate):
    id: int

    class Config:
        from_attributes = True

class RoleUpdate(BaseModel):
    role: str

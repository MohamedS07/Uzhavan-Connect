from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str


class RoleUpdate(BaseModel):
    role: str


class UserOut(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        from_attributes = True

from pydantic import BaseModel

class DonorCreate(BaseModel):
    name: str
    state: str
    email: str
    phone: str
    apply_type: str   # "Occupation / Organization" or "Self"
    occupation_name: str | None = None

class DonorOut(DonorCreate):
    id: int

    class Config:
        from_attributes = True



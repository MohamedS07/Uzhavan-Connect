from pydantic import BaseModel

class NGOCreate(BaseModel):
    ngo_name: str
    registration_number: str
    district: str
    contact_person: str
    contact_number: str
    email: str | None = None
    proof_document: str | None = None

class NGOOut(NGOCreate):
    id: int

    class Config:
        from_attributes = True


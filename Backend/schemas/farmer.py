from pydantic import BaseModel

class FarmerCreate(BaseModel):
    name: str
    village: str
    district: str
    address: str
    phone: str
    loan_amount: str | None = None
    last_date: str | None = None
    bank_account_no: str | None = None
    bank_ifsc: str | None = None
    apply_type: str
    ngo_name: str | None = None

class FarmerOut(FarmerCreate):
    id: int

    class Config:
        from_attributes = True

        from_attributes = True

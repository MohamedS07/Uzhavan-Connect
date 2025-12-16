from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    name = Column(String)
    village = Column(String)
    district = Column(String)
    address = Column(String)
    phone = Column(String)

    loan_amount = Column(String, nullable=True)
    last_date = Column(String, nullable=True)
    bank_account_no = Column(String, nullable=True)
    bank_ifsc = Column(String, nullable=True)

    apply_type = Column(String)
    ngo_name = Column(String, nullable=True)

    photo = Column(String, nullable=True)
    aadhar_photo = Column(String, nullable=True)
    pan_photo = Column(String, nullable=True)
    loan_detail_photo = Column(String, nullable=True)

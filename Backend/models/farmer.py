from sqlalchemy import Column, Integer, String
from database import Base

class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    village = Column(String, nullable=False)
    district = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    loan_amount = Column(String, nullable=True)
    last_date = Column(String, nullable=True)

    bank_account_no = Column(String, nullable=True)
    bank_ifsc = Column(String, nullable=True)

    apply_type = Column(String, nullable=False)
    ngo_name = Column(String, nullable=True)

    photo = Column(String, nullable=True)
    aadhar_photo = Column(String, nullable=True)
    pan_photo = Column(String, nullable=True)
    loan_detail_photo = Column(String, nullable=True)



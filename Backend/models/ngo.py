from sqlalchemy import Column, Integer, String
from database import Base

class NGO(Base):
    __tablename__ = "ngos"

    id = Column(Integer, primary_key=True, index=True)
    ngo_name = Column(String, nullable=False)
    registration_number = Column(String, nullable=False, unique=True)
    district = Column(String, nullable=False)
    contact_person = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    email = Column(String, nullable=True)
    proof_document = Column(String, nullable=True)  # file name / path


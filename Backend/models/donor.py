from sqlalchemy import Column, Integer, String
from database import Base

class Donor(Base):
    __tablename__ = "donors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    apply_type = Column(String, nullable=False)  
    occupation_name = Column(String, nullable=True)



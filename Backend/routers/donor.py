from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.donor import Donor

router = APIRouter(prefix="/donors", tags=["Donors"])

def get_db():
    db = SessionLocal()
    try:    
        yield db
    finally:
        db.close()

@router.post("/")
def create_donor(data: dict, db: Session = Depends(get_db)):
    donor = Donor(**data)
    db.add(donor)
    db.commit()
    return donor

@router.get("/")
def get_donors(db: Session = Depends(get_db)):
    return db.query(Donor).all()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.ngo import NGO

router = APIRouter(prefix="/ngos", tags=["NGOs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_ngo(data: dict, db: Session = Depends(get_db)):
    ngo = NGO(**data)
    db.add(ngo)
    db.commit()
    return ngo

@router.get("/")
def get_ngos(db: Session = Depends(get_db)):
    return db.query(NGO).all()

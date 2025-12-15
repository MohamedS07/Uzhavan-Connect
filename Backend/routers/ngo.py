from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.ngo import NGO
from schemas.ngo import NGOCreate, NGOOut

router = APIRouter(prefix="/ngos", tags=["NGOs"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- POST NGO ----------------
@router.post("/", response_model=NGOOut)
def create_ngo(ngo: NGOCreate, db: Session = Depends(get_db)):
    existing = db.query(NGO).filter(
        NGO.registration_number == ngo.registration_number
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="NGO already registered")

    new_ngo = NGO(**ngo.dict())
    db.add(new_ngo)
    db.commit()
    db.refresh(new_ngo)
    return new_ngo

# ---------------- GET ALL NGOs ----------------
@router.get("/", response_model=list[NGOOut])
def get_all_ngos(db: Session = Depends(get_db)):
    return db.query(NGO).all()

# ---------------- GET NGO BY ID ----------------
@router.get("/{ngo_id}", response_model=NGOOut)
def get_ngo(ngo_id: int, db: Session = Depends(get_db)):
    ngo = db.query(NGO).filter(NGO.id == ngo_id).first()
    if not ngo:
        raise HTTPException(status_code=404, detail="NGO not found")
    return ngo

# ---------------- DELETE NGO ----------------
@router.delete("/{ngo_id}")
def delete_ngo(ngo_id: int, db: Session = Depends(get_db)):
    ngo = db.query(NGO).filter(NGO.id == ngo_id).first()
    if not ngo:
        raise HTTPException(status_code=404, detail="NGO not found")
    db.delete(ngo)
    db.commit()
    return {"message": "NGO deleted successfully"}


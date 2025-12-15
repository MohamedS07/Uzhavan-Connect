from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.donor import Donor
from schemas.donor import DonorCreate, DonorOut

router = APIRouter(prefix="/donors", tags=["Donors"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- POST /donors ----------------
@router.post("/", response_model=DonorOut)
def create_donor(donor: DonorCreate, db: Session = Depends(get_db)):
    new_donor = Donor(**donor.dict())
    db.add(new_donor)
    db.commit()
    db.refresh(new_donor)
    return new_donor

# ---------------- GET /donors ----------------
@router.get("/", response_model=list[DonorOut])
def get_all_donors(db: Session = Depends(get_db)):
    return db.query(Donor).all()

# ---------------- GET /donors/{id} ----------------
@router.get("/{donor_id}", response_model=DonorOut)
def get_donor(donor_id: int, db: Session = Depends(get_db)):
    donor = db.query(Donor).filter(Donor.id == donor_id).first()
    if not donor:
        raise HTTPException(status_code=404, detail="Donor not found")
    return donor

# ---------------- DELETE /donors/{id} ----------------
@router.delete("/{donor_id}")
def delete_donor(donor_id: int, db: Session = Depends(get_db)):
    donor = db.query(Donor).filter(Donor.id == donor_id).first()
    if not donor:
        raise HTTPException(status_code=404, detail="Donor not found")
    db.delete(donor)
    db.commit()
    return {"message": "Donor deleted successfully"}

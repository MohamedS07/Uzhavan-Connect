import os
from fastapi import APIRouter, Depends, Form, UploadFile, File
from sqlalchemy.orm import Session
from database import SessionLocal
from models.farmer import Farmer

router = APIRouter(prefix="/farmers", tags=["Farmers"])
UPLOAD = "uploads/farmers"
os.makedirs(UPLOAD, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def save(file):
    if file:
        path = f"{UPLOAD}/{file.filename}"
        with open(path, "wb") as f:
            f.write(file.file.read())
        return path
    return None

@router.post("/")
def create_farmer(
    user_id: int = Form(...),
    name: str = Form(...),
    village: str = Form(...),
    district: str = Form(...),
    address: str = Form(...),
    phone: str = Form(...),
    apply_type: str = Form(...),
    ngo_name: str = Form(None),
    photo: UploadFile = File(None),
    aadhar_photo: UploadFile = File(None),
    pan_photo: UploadFile = File(None),
    loan_detail_photo: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    farmer = Farmer(
        user_id=user_id,
        name=name,
        village=village,
        district=district,
        address=address,
        phone=phone,
        apply_type=apply_type,
        ngo_name=ngo_name,
        photo=save(photo),
        aadhar_photo=save(aadhar_photo),
        pan_photo=save(pan_photo),
        loan_detail_photo=save(loan_detail_photo)
    )
    db.add(farmer)
    db.commit()
    return {"message": "Farmer registered"}

@router.get("/")
def get_farmers(db: Session = Depends(get_db)):
    return db.query(Farmer).all()

@router.delete("/{id}")
def delete_farmer(id: int, db: Session = Depends(get_db)):
    farmer = db.query(Farmer).get(id)
    db.delete(farmer)
    db.commit()
    return {"message": "Deleted"}

import os
from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from database import SessionLocal
from models.farmer import Farmer

router = APIRouter(prefix="/farmers", tags=["Farmers"])

UPLOAD_DIR = "uploads/farmers"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- POST FARMER WITH FILES ----------------
@router.post("/")
def create_farmer(
    name: str = Form(...),
    village: str = Form(...),
    district: str = Form(...),
    address: str = Form(...),
    phone: str = Form(...),

    loan_amount: str = Form(None),
    last_date: str = Form(None),
    bank_account_no: str = Form(None),
    bank_ifsc: str = Form(None),

    apply_type: str = Form(...),
    ngo_name: str = Form(None),

    photo: UploadFile = File(None),
    aadhar_photo: UploadFile = File(None),
    pan_photo: UploadFile = File(None),
    loan_detail_photo: UploadFile = File(None),

    db: Session = Depends(get_db)
):
    def save_file(file: UploadFile):
        if file:
            file_path = f"{UPLOAD_DIR}/{file.filename}"
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            return file_path
        return None

    farmer = Farmer(
        name=name,
        village=village,
        district=district,
        address=address,
        phone=phone,
        loan_amount=loan_amount,
        last_date=last_date,
        bank_account_no=bank_account_no,
        bank_ifsc=bank_ifsc,
        apply_type=apply_type,
        ngo_name=ngo_name,
        photo=save_file(photo),
        aadhar_photo=save_file(aadhar_photo),
        pan_photo=save_file(pan_photo),
        loan_detail_photo=save_file(loan_detail_photo),
    )

    db.add(farmer)
    db.commit()
    db.refresh(farmer)

    return {"message": "Farmer registered successfully", "farmer_id": farmer.id}

@router.get("/")
def get_all_farmers(db: Session = Depends(get_db)):
    farmers = db.query(Farmer).all()
    return farmers

@router.get("/{farmer_id}")
def get_farmer_by_id(farmer_id: int, db: Session = Depends(get_db)):
    farmer = db.query(Farmer).filter(Farmer.id == farmer_id).first()

    if not farmer:
        return {"error": "Farmer not found"}

    return farmer

@router.delete("/{farmer_id}")
def delete_farmer(farmer_id: int, db: Session = Depends(get_db)):
    farmer = db.query(Farmer).filter(Farmer.id == farmer_id).first()

    if not farmer:
        return {"error": "Farmer not found"}

    # Delete stored files if exist
    for file_path in [
        farmer.photo,
        farmer.aadhar_photo,
        farmer.pan_photo,
        farmer.loan_detail_photo
    ]:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)

    db.delete(farmer)
    db.commit()

    return {"message": "Farmer deleted successfully"}



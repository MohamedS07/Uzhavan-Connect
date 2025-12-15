from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine

from models.user import User
from models.farmer import Farmer
from models.donor import Donor
from models.ngo import NGO

from routers import user, farmer, donor, ngo

app = FastAPI(title="Uzhavan Connect Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(farmer.router)
app.include_router(donor.router)
app.include_router(ngo.router)

@app.get("/")
def root():
    return {"message": "Backend running successfully"}

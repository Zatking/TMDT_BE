from fastapi import APIRouter, Depends, HTTPException,Response,status
from sqlalchemy.orm import Session
from app.database.data import SessionLocal
from app.controller import brand_controller
from pydantic import BaseModel

# Định nghĩa router
router = APIRouter()

# Dependency lấy session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Schema cho Brand
class Brand(BaseModel):
    BrandName: str

# API lấy tất cả các thương hiệu
@router.get("/get_brand")
def get_all_brand(db: Session = Depends(get_db)):
    brands = brand_controller.get_brands(db)
    return brands

# API thêm thương hiệu
@router.post("/create_brand")
def create_brand(brand: Brand, db: Session = Depends(get_db)):
    return brand_controller.create_brand(db, brand)

# API cập nhật thương hiệu
@router.put("/update_brand/{brand_id}")
def update_brand(brand_id: int, brand: Brand, db: Session = Depends(get_db)):
    return brand_controller.update_brand_name(db, brand_id, brand)

# API xóa thương hiệu
@router.delete("/delete_brand/{brand_name}")
def delete_brand(brand_name: str, db: Session = Depends(get_db)):
    return brand_controller.delete_brand(db, brand_name)
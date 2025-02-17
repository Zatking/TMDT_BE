from fastapi import APIRouter, Depends, HTTPException,Response,status
from sqlalchemy.orm import Session
from database.data import SessionLocal
from controller import product_controller
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

#Schema cho Product
class Product(BaseModel):
    ProName: str
    CateID: int
    BrandID: int
    Price: int
    Stock: int
    Description: str

# API lấy tất cả các sản phẩm
@router.get("/get_product")
def get_all_product(db: Session = Depends(get_db)):
    products = product_controller.get_all_products(db)
    return products

# API thêm sản phẩm
@router.post("/create_product")
def create_product(product: Product, db: Session = Depends(get_db)):
    return product_controller.create_product(db, product)

# API cập nhật sản phẩm
@router.put("/update_product/{product_id}")
def update_product(product_id: int, product: Product, db: Session = Depends(get_db)):
    return product_controller.update_product(db, product_id, product)

#API xóa tất cả sản phẩm
@router.delete("/delete_all_product")
def delete_all_product(db: Session = Depends(get_db)):
    return product_controller.delete_all_products(db)

# API xóa sản phẩm
@router.delete("/delete_product/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return product_controller.delete_product(db, product_id)

# API tìm kiếm sản phẩm theo từ khóa
@router.get("/search_product/{keyword}")
def search_product(keyword: str, db: Session = Depends(get_db)):
    products = product_controller.search_product(db, keyword)
    return products
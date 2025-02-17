from fastapi import APIRouter, Depends, HTTPException,Response,status
from sqlalchemy.orm import Session
from database.data import SessionLocal
from controller import cate_controller
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
class Cate(BaseModel):
    CategoryName: str

# API lấy tất cả các danh mục sản phẩm
@router.get("/get_cate")
def get_all_cate(db: Session = Depends(get_db)):
    cates = cate_controller.get_cate(db)
    return cates
# API thêm danh mục sản phẩm
@router.post("/create_cate")
def create_cate(cate: Cate, db: Session = Depends(get_db)):
    return cate_controller.create_cate(db, cate)

# API cập nhật danh mục sản phẩm
@router.put("/update_cate/{cate_id}")
def update_cate(cate_id: int, cate: Cate, db: Session = Depends(get_db)):
    return cate_controller.update_cate(db, cate_id, cate)

# API xóa danh mục sản phẩm
@router.delete("/delete_cate/{cate_id}")
def delete_cate(cate_id: int, db: Session = Depends(get_db)):
    return cate_controller.delete_cate(db, cate_id)




from sqlalchemy.orm import Session
from app.model.model import Category

# Hàm lấy tất cả các danh mục sản phẩm
def get_cate(db: Session):
    try:
        return db.query(Category).all()
    except:
        return ("Khong tim thay danh muc nao")
    
# Hàm tạo danh mục sản phẩm
def create_cate(db: Session, cate_data):
    try:
        if(db.query(Category).filter(Category.CategoryName == cate_data.CategoryName).first()):
            return {"message": "Danh muc da ton tai"}
        else:
            new_cate = Category(**cate_data.dict())
            db.add(new_cate)
            db.commit()
            db.refresh(new_cate)
            return {"message": "Them thanh cong", "Category": new_cate}
    except:
        db.rollback()
        return ("Them that bai")

# Hàm cập nhật danh mục sản phẩm
def update_cate(db: Session, cate_id, cate_data):
    try:
        cate = db.query(Category).filter(Category.CategoryID == cate_id).first()
        if cate:
            for key, value in cate_data:
                setattr(cate, key, value)
            db.commit()
            db.refresh(cate)
            return {"message": "Cap nhat thanh cong", "Category": cate}
        else:
            return {"message": "Khong tim thay danh muc"}
    except:
        db.rollback()
        return ("Cap nhat that bai")
    
    
# Hàm xóa danh mục sản phẩm
def delete_cate(db: Session, cate_id):
    try:
        cate = db.query(Category).filter(Category.CategoryID == cate_id).first()
        if not cate:
            return {"message": "Khong tim thay danh muc"}
        else:
            db.delete(cate)
            db.commit()
            return {"message": "Xoa thanh cong", "Category": cate}
    except:
        db.rollback()
        return ("Xoa that bai")



from sqlalchemy.orm import Session
from model.model import Brand



# Hàm lấy tất cả các thương hiệu
# Hàm này sẽ trả về tất cả các thương hiệu có trong database
def get_brands(db: Session):
    try:
        return db.query(Brand).all()
    except:
        return ("Khong tim thay thuong hieu nao")
    
# Hàm tạo nhãn hàng
# Hàm này sẽ cho phép tạo một thương hiệu mới và chỉ hoạt động khi bạn là admin
def create_brand(db: Session, brand_data):
    try:
        if(db.query(Brand).filter(Brand.BrandName == brand_data.BrandName).first()):
            return {"message": "Brand da ton tai"}
        else:
            new_brand = Brand(**brand_data.dict())
            db.add(new_brand)
            db.commit()
            db.refresh(new_brand)
            return {"message": "Them thanh cong", "Brand": new_brand}
    except:
        db.rollback()
        return ("Them that bai")
    
# Hàm cập nhật thương hiệu
# Hàm này sẽ cho phép cập nhật thông tin của thương hiệu và chỉ hoạt động khi bạn là admin
def update_brand_name(db: Session, brand_id, brand_data):
    try:
        brand = db.query(Brand).filter(Brand.BrandID == brand_id).first()
        if not brand:
            return {"message": "Khong tim thay thuong hieu"}
        else:
            brand.BrandName = brand_data.BrandName
            db.commit()
            db.refresh(brand)
            return {"message": "Cap nhat thanh cong", "Brand": brand}
    except:
        db.rollback()
        return ("Cap nhat that bai")

# Hàm xóa thương hiệu

def delete_brand(db: Session, brand_id):
    try:
        brand = db.query(Brand).filter(Brand.BrandID == brand_id).first()
        if not brand:
            return {"message": "Khong tim thay thuong hieu"}
        else:
            db.delete(brand)
            db.commit()
            return {"message": "Xoa thanh cong", "Brand": brand}
    except:
        db.rollback()
        return ("Xoa that bai")
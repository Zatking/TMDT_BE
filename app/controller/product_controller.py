from sqlalchemy.orm import Session
from model.model import Product


# Hàm lấy tất cả các sản phẩm
def get_all_products(db: Session):
    try:
        return db.query(Product).all()
    except:
        return ("Khong tim thay san pham nao")
    
# Hàm tạo sản phẩm
def create_product(db: Session, product: Product):
    try:
        if(db.query(Product).filter(Product.ProName == product.ProName).first()):
            return ("San pham da ton tai")
        else:
            new_product = Product(**product.dict())
            db.add(new_product)
            db.commit()
            db.refresh(new_product)
            return {"massages":"Them thanh cong", "Product": new_product}
    except InterruptedError:
        db.rollback()
        return ("Them that bai")
    except Exception as e:
        db.rollback()
        print(f"Lỗi khi thêm sản phẩm: {e}")
        return "Thêm thất bại", str(e)


# Hàm cập nhật sản phẩm
def update_product(db: Session, product_id: int, product: Product):
    try:
        product_update = db.query(Product).filter(Product.ProID == product_id).first()
        if product_update:
            for key, value in product.dict().items():
                setattr(product_update, key, value)
            db.commit()
            db.refresh(product_update)
            return {"message": "Cập nhật thành công", "Product": product_update}
        else:
            return {"message": "Không tìm thấy sản phẩm"}
    except InterruptedError:
        db.rollback()
        return ("Cập nhật thất bạibại")
    except Exception as e:
        db.rollback()
        print(f"Lỗi khi cập nhật sản phẩm: {e}")
        return "Cập nhật sản phẩm thất bại", str(e)
    
# Hàm xóa sản phẩm
def delete_product(db: Session, product_id: int):
    try:
        product = db.query(Product).filter(Product.ProID == product_id).first()
        if not product:
            return ("Khong tim thay san pham")  
        else:
            db.delete(product)
            db.commit()
            return ("Xoa thanh cong")
    except InterruptedError:
        db.rollback()
        return ("Them that bai")
    except Exception as e:
        db.rollback()
        print(f"Lỗi khi xóa sản phẩm : {e}")
        return "Xóa thất bại", str(e)
    
# Hàm xóa tất cả  sản phẩm
def delete_all_products(db: Session):   
    try:
        products = db.query(Product).all()
        for product in products:
            db.delete(product)
        db.commit()
        return ("Xóa thành công tất cả sản phẩm ")
    except:
        db.rollback()
        return ("Xóa thất bại tất cả sản phẩm")
    

# Hàm tìm kiếm sản phẩm theo từ khóa
def search_product(db: Session, keyword: str):
    if(keyword == ""):
        return ("Vui lòng nhập từ khóa")
    try:
        products = db.query(Product).filter(Product.ProName.like(f"%{keyword}%")).all()
        if not products:
            return ("Không tìm thấy sản phẩm")
        else:
            return products
    except Exception as e:
        db.rollback()
        print(f"Lỗi khi tìm kiếm sản phẩm: {e}")
        return "Tìm kiếm sản phẩm thất bại", str(e)

# Hàm lọc sản phẩm
def filter_product(db: Session, category: str, price: str):
    try:
        if category == "all" and price == "all":
            products = db.query(Product).all()
            return products
        elif category == "all":
            products = db.query(Product).filter(Product.Price <= int(price)).all()
            return products
        elif price == "all":
            products = db.query(Product).filter(Product.CateID == int(category)).all()
            return products
        else:
            products = db.query(Product).filter(Product.CateID == int(category), Product.Price <= int(price)).all()
            return products
    except Exception as e:
        db.rollback()
        print(f"Lỗi khi lọc sản phẩm: {e}")
        return "Lọc sản phẩm thất bại", str(e)
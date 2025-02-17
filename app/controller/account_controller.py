from sqlalchemy.orm import Session
from model.model import Account,Admin


#APi tạo tài khoản admin
def create_admin(db: Session, admin: Admin):
    try:
        if(db.query(Admin).filter(Admin.Username == admin.Username).first()):
            return {"message": "Admin da ton tai"}
        else:
            new_admin = Admin(**admin.dict())
            db.add(new_admin)
            db.commit()
            db.refresh(new_admin)
            return {"message": "Them thanh cong", "Admin": new_admin}
    except:
        db.rollback()
        return ("Them that bai")

#API lấy tất cả tài khoản admin
def get_all_admin(db: Session):
    try:
        return db.query(Admin).all()
    except:
        return ("Khong tim thay admin nao")

#API cập nhật tài khoản admin
def update_admin(db: Session, admin: Admin, admin_id: int):
    try:
        admin_update = db.query(Admin).filter(Admin.AdminID == admin_id).first()
        if admin_update:
            for key, value in admin.dict().items():
                setattr(admin_update, key, value)
            db.commit()
            db.refresh(admin_update)
            return {"message": "Cập nhật thành công", "Admin": admin_update}
        else:
            return {"message": "Không tìm thấy admin"}
    except:
        db.rollback()
        return ("Cập nhật thất bạibại")
    
#API tạo tài khoản người dùng
def create_account(db: Session, account: Account):
    try:
        if(db.query(Account).filter(Account.Username == account.Username).first()):
            return {"message": "Account da ton tai"}
        else:
            new_account = Account(**account.dict())
            db.add(new_account)
            db.commit()
            db.refresh(new_account)
            return {"message": "Them thanh cong", "Account": new_account}
    except:
        db.rollback()
        return ("Them that bai")

#API lấy tất cả tài khoản người dùng
def get_all_account(db: Session):
    try:
        return db.query(Account).all()
    except:
        return ("Khong tim thay account nao")

#Api cập nhật tài khoản người dùng
def update_account(db: Session, account: Account, account_id: int):
    try:
        account_update = db.query(Account).filter(Account.AccountID == account_id).first()
        if account_update:
            for key, value in account.dict().items():
                setattr(account_update, key, value)
            db.commit()
            db.refresh(account_update)
            return {"message": "Cập nhật thành công", "Account": account_update}
        else:
            return {"message": "Không tìm thấy account"}
    except:
        db.rollback()
        return ("Cập nhật thất bại")
    
#API tìm kiếm tài khoản theo username
def search_account(db: Session, username: str):
    if (username =="" or username == None):
        return {"message": "Nhập lại từ khóa"}
    try:
        account = db.query(Account).filter(Account.Username == username).first()
        if account:
            return account
        else:
            return {"message": "Không tìm thấy account"}
    except Exception as e:
        db.rollback()
        print(f"Lỗi khi account: {e}")
        return "Tìm sảnsản phẩm thất bại", str(e)



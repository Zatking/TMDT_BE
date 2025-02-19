from fastapi import APIRouter, Depends, HTTPException,Response,status
from app.database.data import SessionLocal
from app.controller import account_controller
from sqlalchemy.ext.asyncio import AsyncSession
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

#Schema cho AccountAdmin 
class AccountAdmin(BaseModel):
    UserName: str
    Password: str

#Schema cho AccountUser
class AccountUser(BaseModel):
    Username = str
    Password = str
    FullName = str
    Email = str
    Phone = str
    Birthday = str
    Address = str

# API lấy tất cả các tài khoản admin
@router.get("/get_admin")
async def get_all_admin(db: Session = Depends(get_db)):
    admins = account_controller.get_all_admin(db)
    return admins

# API thêm tài khoản admin
@router.post("/create_admin")
def create_admin(admin: AccountAdmin, db: Session = Depends(get_db)):
    return account_controller.create_admin(db, admin)

# API cập nhật tài khoản admin
@router.put("/update_admin/{admin_id}")
def update_admin(admin_id: int, admin: AccountAdmin, db: Session = Depends(get_db)):
    return account_controller.update_admin(db, admin, admin_id)

#API lấy tất cả tài khoản người dùng
@router.get("/get_account")
def get_all_account(db: Session = Depends(get_db)):
    accounts = account_controller.get_all_account(db)
    return accounts

#API tạo tài khoản người dùng
@router.post("/create_account")
def create_account(account: AccountUser, db: Session = Depends(get_db)):
    return account_controller.create_account(db, account)

#API cập nhật tài khoản người dùng
@router.put("/update_account/{account_id}")
def update_account(account_id: int, account: AccountUser, db: Session = Depends(get_db)):
    return account_controller.update_account(db, account, account_id)

#API tìm kiếm tài khoản theo từ khóa
@router.get("/search_account/{username}")
def search_account(username: str, db: Session = Depends(get_db)):
    accounts = account_controller.search_account(db, username)
    return accounts

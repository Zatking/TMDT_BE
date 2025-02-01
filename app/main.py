from fastapi import FastAPI
from app.router import brand_router,cate_router,product_router
from app.database.data import Base, engine

# Tạo bảng trong database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD Example with SQL Server")


# Đăng ký router
app.include_router(brand_router.router, prefix="/api", tags=["brands"])
app.include_router(cate_router.router, prefix="/api", tags=["categories"])
app.include_router(product_router.router, prefix="/api", tags=["products"])


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with SQL Server 2/2"}

@app.get("/Hello")
def Hello():
    return {"message": "Hello World Mr.Thanh"}



from router import brand_router,cate_router,product_router
from database.data import Base, engine
from fastapi import FastAPI

# Tạo bảng trong database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD Example with SQL Server")


# Đăng ký router
app.include_router(brand_router.router, prefix="/api", tags=["brands"])
app.include_router(cate_router.router, prefix="/api", tags=["categories"])
app.include_router(product_router.router, prefix="/api", tags=["products"])


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with SQL Server On Vercel"}

@app.get("/Hello")
def Hello():
    return {"message": "Hello World Mr.Thanh HUFLIT k28"}


@app.get("/VercelTest")
def VercelTest():
    return {"message": "Vercel Testing"}


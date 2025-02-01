from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cấu hình kết nối đến SQL Server
DATABASE_URL = "mssql+pyodbc://sa:123@Zatk/BETMDT?driver=ODBC+Driver+17+for+SQL+Server"

# Tạo engine kết nối
engine = create_engine(DATABASE_URL)

# Tạo session để truy vấn dữ liệu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model để kế thừa
Base = declarative_base()

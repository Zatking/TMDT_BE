from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database.data import Base

# Định nghĩa bảng Category
class Category(Base):
    __tablename__ = "CATEGORIES"  # Giữ nguyên chữ hoa giống SQL Server

    CategoryID = Column(Integer, primary_key=True, index=True)
    CategoryName = Column(String, index=True)

    # Liên kết với bảng Product
    products = relationship("Product", back_populates="category")

# Định nghĩa bảng Brand
class Brand(Base):
    __tablename__ = "BRAND"  # Giữ nguyên chữ hoa giống SQL Server

    BrandID = Column(Integer, primary_key=True, index=True)
    BrandName = Column(String, index=True)

    # Liên kết với bảng Product
    products = relationship("Product", back_populates="brand")

# Định nghĩa bảng Product
class Product(Base):
    __tablename__ = "PRODUCTS"  # Giữ nguyên chữ hoa giống SQL Server

    ProID = Column(Integer, primary_key=True, index=True)
    ProName = Column(String, index=True)

    CateID = Column(Integer, ForeignKey("CATEGORIES.CategoryID"))  # Giữ nguyên chữ hoa
    category = relationship("Category", back_populates="products")

    BrandID = Column(Integer, ForeignKey("BRAND.BrandID"))  # Giữ nguyên chữ hoa
    brand = relationship("Brand", back_populates="products")

    Price = Column(Integer)
    Stock = Column(Integer)
    Description = Column(String)

#Định nghĩa bảng account
class Account(Base):
    __tablename__ = "ACCOUNT"  # Giữ nguyên chữ hoa giống SQL Server

    AccountID = Column(Integer, primary_key=True, index=True)
    Username = Column(String, index=True)
    Password = Column(String, index=True)
    FullName = Column(String, index=True)
    Email = Column(String, index=True)
    Phone = Column(String, index=True)
    Birthday = Column(String, index=True)
    Address = Column(String, index=True)
   
     # Liên kết với bảng Order
    orders = relationship("Order", back_populates="account")

#Định nghĩa bảng Admin
class Admin(Base):
    __tablename__ = "ADMIN"  # Giữ nguyên chữ hoa giống SQL Server
    AdminID = Column(Integer, primary_key=True, index=True)
    Username = Column(String, index=True)
    Password = Column(String, index=True)


#Định nghĩa bảng Order

class Order(Base):
    __tablename__ = "ORDER"  # Giữ nguyên chữ hoa giống SQL Server
    OrderID = Column(Integer, primary_key=True, index=True)
    AccountID = Column(Integer, ForeignKey("ACCOUNT.AccountID"))  # Giữ nguyên chữ hoa
    OrderDate = Column(Date)
    TotalAmount = Column(Integer)
    Status = Column(String, index=True)

#Định nghĩa bảng OrderDetail

class OrderDetail(Base):
    __tablename__ = "ORDERDETAIL"  # Giữ nguyên chữ hoa giống SQL Server
    OrderDetailID = Column(Integer, primary_key=True, index=True)
    OrderID = Column(Integer, ForeignKey("ORDER.OrderID"))  # Giữ nguyên chữ hoa
    ProductID = Column(Integer, ForeignKey("PRODUCTS.ProID"))  # Giữ nguyên chữ hoa
    Quantity = Column(Integer)
    Price = Column(Integer)
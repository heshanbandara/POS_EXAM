from datetime import datetime
from typing import List

from sqlalchemy import Integer, String, Boolean, Float, Numeric, ForeignKey, DateTime, func
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Category(Base):

    __tablename__ = "category"

    category_id:Mapped[int] =  mapped_column(Integer,primary_key=True,index=True)
    category_code:Mapped[int] = mapped_column(Integer,unique=True,index=True,nullable=False)
    category_name:Mapped[str] = mapped_column(String(30),nullable=False)
    description:Mapped[str] = mapped_column(String(100),nullable=False)
    active:Mapped[bool] = mapped_column(Boolean,default=True)

    product:Mapped[List["Product"]] = relationship(
        back_populates="category",
        cascade="all,delete-orphan",
        lazy="selectin"
    )

class Product(Base):


    __tablename__ = "product"

    product_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_code: Mapped[int] = mapped_column(Integer,nullable=False,unique=True)
    product_name: Mapped[str] = mapped_column(String(100),nullable=False)
    unit_price : Mapped[float] = mapped_column(Numeric(12, 2), nullable=False,ge=0)
    available_quantity : Mapped[int] = mapped_column(Integer,nullable=False,ge=0)
    active:Mapped[str] = mapped_column(String(50), default="AVAILABLE", server_default="AVAILABLE", nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("category_id", ondelete="CASCADE"), nullable=False, index=True
    )

    customer: Mapped[List["Customer"]] = relationship(
        back_populates="product",
        cascade="all,delete-orphan",
        lazy="selectin"
    )

class Customer(Base):

    __tablename__ = "customer"

    customer_id:Mapped[int] = mapped_column(String(30),nullable=False)
    mobile_number:Mapped[str] = mapped_column(TEXT(50),nullable=False,unique=True)
    full_name:Mapped[str] = mapped_column(String(100),nullable=False)
    email:Mapped[str] = mapped_column(String(100),nullable=False)
    loyalty_points:Mapped[float] = mapped_column(Float,nullable=False)
    registered_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now(), nullable=False)

    customer: Mapped["Customer"] = relationship(
        back_populates="order",
        lazy="joined"
    )




class Order(Base):

    __tablename__ = "order"

    order_id:Mapped[int] = mapped_column(Integer,nullable=False,index=True)
    customer_id:Mapped[int] = mapped_column(
        ForeignKey("customer_id", ondelete="CASCADE"), nullable=False, index=True
    )
    order_date_time:Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now(), nullable=False)
    order_status:Mapped[str] = mapped_column(String(50), default="COMPLETED ", server_default="COMPLETED ", nullable=False)

















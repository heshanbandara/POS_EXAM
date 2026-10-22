from datetime import datetime

from sqlalchemy import String, TEXT, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Customer(Base):

    __tablename__ = "customer"

    customer_id:Mapped[int] = mapped_column(String(30),nullable=False)
    mobile_number:Mapped[str] = mapped_column(TEXT(50),nullable=False,unique=True)
    full_name:Mapped[str] = mapped_column(String(100),nullable=False)
    email:Mapped[str] = mapped_column(String(100),nullable=False)
    loyalty_points:Mapped[float] = mapped_column(Float,nullable=False)
    registered_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now(), nullable=False)
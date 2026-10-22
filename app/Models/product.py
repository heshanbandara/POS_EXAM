from sqlalchemy import Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


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

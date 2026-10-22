from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Category(Base):

    __tablename__ = "category"

    category_id:Mapped[int] =  mapped_column(Integer,primary_key=True,index=True)
    category_code:Mapped[int] = mapped_column(Integer,unique=True,index=True,nullable=False)
    category_name:Mapped[str] = mapped_column(String(30),nullable=False)
    description:Mapped[str] = mapped_column(String(100),nullable=False)
    active:Mapped[bool] = mapped_column(Boolean,default=True)



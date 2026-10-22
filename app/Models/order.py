from datetime import datetime

from sqlalchemy import ForeignKey, Integer, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Order(Base):

    __tablename__ = "order"

    order_id:Mapped[int] = mapped_column(Integer,nullable=False,index=True)
    customer_id:Mapped[int] = mapped_column(
        ForeignKey("customer_id", ondelete="CASCADE"), nullable=False, index=True
    )
    order_date_time:Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now(), nullable=False)
    order_status:Mapped[str] = mapped_column(String(50), default="COMPLETED ", server_default="COMPLETED ", nullable=False)
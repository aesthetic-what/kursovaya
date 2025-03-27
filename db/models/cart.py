from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from db.db_core import Base
from datetime import datetime


class Cart(Base):
    __tablename__ = "cart"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    status: Mapped[str] = mapped_column(nullable=False, default="awaiting payment")
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow, index=True)
    items = relationship("CartItem", back_populates="cart")

    def __repr__(self) -> str:
        return f"Cart(id={self.id}, user_id={self.user_id}, status={self.status})"
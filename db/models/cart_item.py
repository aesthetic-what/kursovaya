from sqlalchemy import ForeignKey, Numeric, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from decimal import Decimal
from db.db_core import Base

class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey("cart.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    product_count: Mapped[int] = mapped_column(nullable=False)  # Количество товаров теперь целое число
    summary: Mapped[int] = mapped_column(index=True, nullable=True)  # Общая стоимость теперь целое числo
    cart = relationship("Cart", back_populates="items")
    product = relationship("Products")

    def __repr__(self) -> str:
        return f"CartItem(id={self.id}, cart_id={self.cart_id}, product_id={self.product_id}, count={self.product_count})"
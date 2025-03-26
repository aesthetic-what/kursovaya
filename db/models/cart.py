from sqlalchemy.orm import Mapped, mapped_column
from db.db_core import Base


class Cart(Base):
    __tablename__ = "carts"
    id: Mapped[int] = mapped_column(autoincrement=True)
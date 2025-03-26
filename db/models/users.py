from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from db.db_core import Base

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(autoincrement=True)
    login: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str]
    last_name: Mapped[str]
    number: Mapped[str]
    city: Mapped[str]
    id_cart: Mapped[int] = mapped_column(ForeignKey("carts.id"), nullable=True)


class Cart(Base):
    __tablename__ = "carts"
    id: Mapped[int] = mapped_column(autoincrement=True)



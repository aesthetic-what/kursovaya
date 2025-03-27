from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, LargeBinary
from db.db_core import Base

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str]
    last_name: Mapped[str]
    number: Mapped[str]
    city: Mapped[str]
    balance: Mapped[int]
    photo: Mapped[bytes] = mapped_column(LargeBinary)
    # id_cart: Mapped[int] = mapped_column(ForeignKey("carts.id"), nullable=True)


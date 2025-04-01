from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, LargeBinary
from db.db_core import Base

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    number: Mapped[str] = mapped_column(nullable=True)
    city: Mapped[str] = mapped_column(nullable=True)
    balance: Mapped[int] = mapped_column(default=0)
    photo: Mapped[bytes] = mapped_column(LargeBinary, nullable=True)
    role: Mapped[str] = mapped_column(default='user')
    # id_cart: Mapped[int] = mapped_column(ForeignKey("carts.id"), nullable=True)


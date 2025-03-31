from sqlalchemy import LargeBinary
from sqlalchemy.orm import Mapped, mapped_column
from db.db_core import Base
from datetime import datetime

class Products(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    importer: Mapped[str] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(default=0)
    date_add: Mapped[datetime]
    photo: Mapped[bytes] = mapped_column(LargeBinary, nullable=True)
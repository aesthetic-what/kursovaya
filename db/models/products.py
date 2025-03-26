from sqlalchemy.orm import Mapped, mapped_column
from db.db_core import Base
from datetime import datetime

class Products(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    importer: Mapped[str] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(default=0)
    date_add: Mapped[datetime]
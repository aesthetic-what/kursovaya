from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

con_str = "postgresql+psycopg2://postgres:pass@localhost:5432/shop_db"

engine = create_engine(con_str)

local_session = sessionmaker(engine)


class Base(DeclarativeBase): pass
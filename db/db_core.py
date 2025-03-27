from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


con_str = "postgresql+psycopg2://postgres:pass@aestheticperforator.ru:5432/kursovaya"

engine = create_engine(con_str, echo=True)

local_session = sessionmaker(engine)


class Base(DeclarativeBase): pass

def init_db():
    Base.metadata.create_all(engine)
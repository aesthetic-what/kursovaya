from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


con_str = "sqlite:///kursovaya.db"

engine = create_engine(con_str)

local_session = sessionmaker(engine)


class Base(DeclarativeBase): pass

def init_db():
    Base.metadata.create_all(engine)
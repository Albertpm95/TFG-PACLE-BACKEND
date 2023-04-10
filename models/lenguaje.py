from sqlalchemy import Column, String, Integer
from db.database import Base


class Lenguaje(Base):
    __tablename__: str = "lenguajes"

    idLenguaje = Column(Integer, primary_key=True)
    lenguaje = Column(String, nullable=False, unique=True)

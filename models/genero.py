from sqlalchemy import Column, String, Integer
from db.database import Base


class Genero(Base):
    __tablename__ = "generos"

    idGenero = Column(Integer, primary_key=True)
    genero = Column(String, nullable=False, unique=True)

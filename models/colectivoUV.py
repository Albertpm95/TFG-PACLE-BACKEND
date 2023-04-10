from sqlalchemy import Column, String, Integer
from db.database import Base


class Genero(Base):
    __tablename__ = "colectivoUV"

    idColectivo = Column(Integer, primary_key=True)
    colectivo = Column(String, nullable=False, unique=True)

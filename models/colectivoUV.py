from sqlalchemy import Column, String, Integer
from db.database import Base


class ColectivoUV(Base):
    __tablename__: str = "colectivoUV"

    idColectivoUV = Column(Integer, primary_key=True)
    colectivoUV = Column(String, nullable=False, unique=True)

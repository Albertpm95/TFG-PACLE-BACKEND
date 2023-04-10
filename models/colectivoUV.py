from sqlalchemy import Column, String, Integer
from db.database import Base


class ColectivoUV(Base):
    __tablename__: str = "colectivoUV"

    idColectivo = Column(Integer, primary_key=True)
    colectivo = Column(String, nullable=False, unique=True)

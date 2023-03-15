from sqlalchemy import Column, String, Integer
from db.database import Base


class Nivel(Base):
    __tablename__ = "niveles"

    idNivel = Column(Integer, primary_key=True)
    nivel = Column(String, nullable=False)

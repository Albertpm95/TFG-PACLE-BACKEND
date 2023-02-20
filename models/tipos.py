from sqlalchemy import Column, String, Integer
from db.database import Base


class Tipos(Base):
    __tablename__ = "tipos"

    id_tipo = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)

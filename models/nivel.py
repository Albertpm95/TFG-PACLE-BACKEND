from sqlalchemy import Column, String, Integer
from db.database import Base


class Nivel(Base):
    __tablename__ = "niveles"

    id_nivel = Column(Integer, primary_key=True)
    nivel = Column(String, nullable=False)

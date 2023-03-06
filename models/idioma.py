from sqlalchemy import Column, String, Integer
from db.database import Base


class Idioma(Base):
    __tablename__ = "idiomas"

    id_lenguaje = Column(Integer, primary_key=True)
    lenguaje = Column(String, nullable=False)

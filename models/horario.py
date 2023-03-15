from sqlalchemy import Column, String, Integer
from db.database import Base


class Horario(Base):
    __tablename__ = "horarios"

    idHorario = Column(Integer, primary_key=True)
    horario = Column(String, nullable=False, unique=True)

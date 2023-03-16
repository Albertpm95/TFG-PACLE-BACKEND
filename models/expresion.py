from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from db.database import Base
from models.shared import ParteExpresion

from models.tarea import Tarea
from schemas.tarea import TareasExpresion


class Expresion(Base):
    __tablename__ = "expresion"

    idExpresion = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    observaciones = Column(String, nullable=True)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntosConseguidos = Column(Integer, nullable=False, default=0)
    puntuacionMaxima = Column(Integer, nullable=False, default=0)
    idParte1 = Column(Integer, ForeignKey("parte_expresion.idParte"))
    parte1: Mapped[ParteExpresion] = relationship()
    idParte2 = Column(Integer, ForeignKey("parte_expresion.idParte"))
    parte2: Mapped[ParteExpresion] = relationship()

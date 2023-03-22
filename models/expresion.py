from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship

from db.database import Base
from models.shared import Correccion
from models.tarea import Tarea
from schemas.tarea import ListaTareas


class Expresion(Base):
    __tablename__ = "expresion"

    idActa = Column(Integer, ForeignKey("actas.idActa"))
    idExpresion = Column(Integer, primary_key=True)
    idParte1 = Column(Integer, ForeignKey("correccion.idCorreccion"))
    idParte2 = Column(Integer, ForeignKey("correccion.idCorreccion"))
    observaciones = Column(String, nullable=True)
    parte1: Mapped[Correccion] = relationship()
    parte2: Mapped[Correccion] = relationship()
    porcentaje = Column(Integer, nullable=False, default=0)
    puntosConseguidos = Column(Integer, nullable=False, default=0)
    puntuacionMaxima = Column(Integer, nullable=False, default=0)
    tipo = Column(String, nullable=False)

    UniqueConstraint(idActa, tipo)


"""    idParte1 = Column(Integer, ForeignKey("parte_expresion.idParte"))
    parte1: Mapped[ParteExpresion] = relationship()
    idParte2 = Column(Integer, ForeignKey("parte_expresion.idParte"))
    parte2: Mapped[ParteExpresion] = relationship()"""

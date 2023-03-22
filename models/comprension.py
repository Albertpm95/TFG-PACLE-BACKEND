from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped
from db.database import Base
from models.tarea import Tarea


class Comprension(Base):
    __tablename__ = "comprension"

    idComprension = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    observaciones = Column(String, nullable=True)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntosConseguidos = Column(Integer, nullable=False, default=0)
    puntuacionMaxima = Column(Integer, nullable=False, default=0)
    idParte = Column(Integer, ForeignKey("correccion.idCorreccion"))
    idActa = Column(Integer, ForeignKey("actas.idActa"))

    UniqueConstraint(idActa, tipo)

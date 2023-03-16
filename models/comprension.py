from sqlalchemy import Column, Integer, String, ForeignKey
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
    idCorrector = Column(Integer, ForeignKey("usuarios.idUsuario"))
    idTarea = Column(Integer, ForeignKey("tareas.idTarea"))
    tareas: Mapped[list[Tarea]] = relationship()

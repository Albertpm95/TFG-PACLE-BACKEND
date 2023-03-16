from sqlalchemy import Column, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship, Mapped

from db.database import Base
from models.horario import Horario
from models.lenguaje import Lenguaje
from models.nivel import Nivel


class Convocatoria(Base):
    __tablename__ = "convocatorias"

    maxComprensionLectora = Column(Integer, nullable=False)
    maxComprensionAuditiva = Column(Integer, nullable=False)
    maxExpresionEscrita = Column(Integer, nullable=False)
    maxExpresionOral = Column(Integer, nullable=False)
    idConvocatoria = Column(Integer, primary_key=True, index=True)
    idLenguaje = Column(Integer, ForeignKey("lenguajes.idLenguaje"))
    lenguaje: Mapped[Lenguaje] = relationship()
    fecha = Column(DateTime, nullable=False)
    idHorario = Column(Integer, ForeignKey("horarios.idHorario"))
    horario: Mapped[Horario] = relationship()
    estado = Column(Boolean, nullable=False, default=True)
    idNivel = Column(Integer, ForeignKey("niveles.idNivel"))
    nivel: Mapped[Nivel] = relationship()

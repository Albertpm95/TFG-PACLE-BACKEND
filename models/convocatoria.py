from sqlalchemy import Column, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship, Mapped

from db.database import Base
from models.horario import Horario
from models.idioma import Idioma


class Convocatoria(Base):
    __tablename__ = "convocatorias"

    comprension_auditiva_puntuacion_maxima_parte = Column(
        Integer(), nullable=False, default=0
    )
    comprension_lectora_puntuacion_maxima_parte = Column(
        Integer(), nullable=False, default=0
    )
    expresion_escrita_puntuacion_maxima_parte = Column(
        Integer(), nullable=False, default=0
    )
    expresion_oral_puntuacion_maxima_parte = Column(
        Integer(), nullable=False, default=0
    )
    id_convocatoria = Column(Integer, primary_key=True, index=True)
    id_lenguaje = Column(Integer, ForeignKey("idiomas.id_lenguaje"))
    lenguaje: Mapped[Idioma] = relationship()
    fecha = Column(DateTime, nullable=False)
    id_horario = Column(Integer, ForeignKey("horarios.id_horario"))
    horario: Mapped[Horario] = relationship()
    estado = Column(Boolean, nullable=False, default=True)

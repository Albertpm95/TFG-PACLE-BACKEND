from sqlalchemy import Column, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship, Mapped

from db.database import Base
from models.horario import Horario
from models.lenguaje import Lenguaje
from models.nivel import Nivel


class Convocatoria(Base):
    __tablename__ = "convocatorias"

    maximo_comprension_lectora = Column(Integer, nullable=False)
    maximo_comprension_auditiva = Column(Integer, nullable=False)
    maximo_expresion_escrita = Column(Integer, nullable=False)
    maximo_expresion_oral = Column(Integer, nullable=False)
    id_convocatoria = Column(Integer, primary_key=True, index=True)
    id_lenguaje = Column(Integer, ForeignKey("lenguajes.id_lenguaje"))
    lenguaje: Mapped[Lenguaje] = relationship()
    fecha = Column(DateTime, nullable=False)
    id_horario = Column(Integer, ForeignKey("horarios.id_horario"))
    horario: Mapped[Horario] = relationship()
    estado = Column(Boolean, nullable=False, default=True)
    id_nivel = Column(Integer, ForeignKey("niveles.id_nivel"))
    nivel: Mapped[Nivel] = relationship()

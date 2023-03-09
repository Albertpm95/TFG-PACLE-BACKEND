from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship, Mapped

from db.database import Base
from models.alumno import Alumno
from models.convocatoria import Convocatoria


class Acta(Base):
    __tablename__ = "actas"

    id_convocatoria = Column(Integer, ForeignKey("convocatorias.id_convocatoria"))
    convocatoria: Mapped[Convocatoria] = relationship()
    fecha = Column(DateTime, nullable=False)
    id_acta = Column(Integer, primary_key=True, index=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id_alumno"))
    alumno: Mapped[Alumno] = relationship()
    expresion_escrita = Column(Integer, ForeignKey("expresion.id_expresion"))
    expresion_oral = Column(Integer, ForeignKey("expresion.id_expresion"))
    comprension_lectiva = Column(Integer, ForeignKey("comprension.id_comprension"))
    comprension_auditiva = Column(Integer, ForeignKey("comprension.id_comprension"))

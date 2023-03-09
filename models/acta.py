from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column

from db.database import Base
from models.alumno import Alumno
from models.convocatoria import Convocatoria
from models.expresion_escrita import ExpresionEscrita
from models.expresion_oral import ExpresionOral
from models.comprension_auditiva import ComprensionAuditiva
from models.comprension_lectora import ComprensionLectora


class Acta(Base):
    __tablename__ = "actas"

    id_acta = Column(Integer, primary_key=True)
    id_convocatoria = Column(Integer, ForeignKey("convocatorias.id_convocatoria"))
    convocatoria: Mapped[Convocatoria] = relationship()
    id_alumno = Column(Integer, ForeignKey("alumnos.id_alumno"))
    alumno: Mapped[Alumno] = relationship()
    fecha = Column(DateTime, nullable=False)
    id_expresion_escrita = Column(Integer, ForeignKey("expresion_escrita.id_expresion"))
    expresion_escrita: Mapped[ExpresionEscrita] = relationship()
    id_expresion_oral = Column(Integer, ForeignKey("expresion_oral.id_expresion"))
    expresion_oral: Mapped[ExpresionOral] = relationship()
    id_comprension_lectora = Column(
        Integer, ForeignKey("comprension_lectora.id_comprension")
    )
    comprension_lectora: Mapped[ComprensionLectora] = relationship()
    id_comprension_auditiva = Column(
        Integer, ForeignKey("comprension_auditiva.id_comprension")
    )
    comprension_auditiva: Mapped[ComprensionAuditiva] = relationship()

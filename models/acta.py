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

    idActa = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)

    idConvocatoria = Column(Integer, ForeignKey("convocatorias.idConvocatoria"))
    convocatoria: Mapped[Convocatoria] = relationship()

    idAlumno = Column(Integer, ForeignKey("alumnos.idAlumno"))
    alumno: Mapped[Alumno] = relationship()

    idExpresionEscrita = Column(Integer, ForeignKey("expresion_escrita.idExpresion"))
    expresionEscrita: Mapped[ExpresionEscrita] = relationship()

    idExpresionOral = Column(Integer, ForeignKey("expresion_oral.idExpresion"))
    expresion_oral: Mapped[ExpresionOral] = relationship()

    idComprensionLectora = Column(
        Integer, ForeignKey("comprension_lectora.idComprension")
    )
    comprensionLectora: Mapped[ComprensionLectora] = relationship()

    idComprensionAuditiva = Column(
        Integer, ForeignKey("comprension_auditiva.idComprension")
    )
    comprensionAuditiva: Mapped[ComprensionAuditiva] = relationship()

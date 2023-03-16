from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship, Mapped
from db.database import Base
from models.convocatoria import Convocatoria
from models.expresion import Expresion
from models.comprension import Comprension
from models.shared import AlumnosActa


class Acta(Base):
    __tablename__ = "actas"

    idActa = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)

    idConvocatoria = Column(Integer, ForeignKey("convocatorias.idConvocatoria"))
    convocatoria: Mapped[Convocatoria] = relationship()

    idExpresionEscrita = Column(Integer, ForeignKey("expresion.idExpresion"))
    expresionEscrita: Mapped[Expresion] = relationship()

    idExpresionOral = Column(Integer, ForeignKey("expresion.idExpresion"))
    expresion_oral: Mapped[Expresion] = relationship()

    idComprensionLectora = Column(Integer, ForeignKey("comprension.idComprension"))
    comprensionLectora: Mapped[Comprension] = relationship()

    idComprensionAuditiva = Column(Integer, ForeignKey("comprension.idComprension"))
    comprensionAuditiva: Mapped[Comprension] = relationship()

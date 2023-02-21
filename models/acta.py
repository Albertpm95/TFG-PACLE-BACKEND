from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from db.database import Base


class Acta(Base):
    __tablename__ = "actas"

    comprension = relationship("Comprension", back_populates="acta")
    convocatoria = Column(Integer, ForeignKey("convocatorias.id_convocatoria"))
    expresion = relationship("Expresion", back_populates="acta")
    fecha = Column(DateTime, nullable=False)
    id_acta = Column(Integer, primary_key=True, index=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id_alumno"))

    comprensiones = relationship("Expresion", back_populates="acta")
    expresiones = relationship("Expresion", back_populates="acta")

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship

from .database import Base

presentados_acta = Table(
    "presentados_acta",
    Column("id_alumno", ForeignKey("alumnos.id"), primary_key=True),
    Column("id_acta", ForeignKey("actas.id"), primary_key=True)
)


class Acta(Base):
    __tablename__ = 'actas'

    id = Column(String, primary_key=True, index=True)
    lenguage = Column(String)
    tipo = Column(String)
    fecha = Column(DateTime)
    presentados = relationship(
        "Alumno", secondary=presentados_acta, back_populates=True)


class Alumno(Base):
    __tablename__ = 'alumnos'

    id = Column(String, primary_key=True, index=True)
    nombre = Column(String)
    apellidos = Column(String)
    examinado_convocatorias = relationship(
        "Acta", secondary=presentados_acta, back_populates=True)

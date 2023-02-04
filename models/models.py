from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship

import db.session as session

presentados_acta = Table(
    "presentados_acta",
    session.Base.metadata,
    Column("id_alumno", ForeignKey("alumnos.id"), primary_key=True),
    Column("id_acta", ForeignKey("actas.id"), primary_key=True)
)


class Acta(session.Base):
    __tablename__ = 'actas'

    id = Column(String, primary_key=True, index=True)
    lenguage = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    fecha = Column(DateTime, nullable=False)
    presentados = relationship(
        "Alumno", secondary=presentados_acta, back_populates=True)


class Alumno(session.Base):
    __tablename__ = 'alumnos'

    id = Column(String, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    examinado_convocatorias = relationship(
        "Acta", secondary=presentados_acta, back_populates=True)


class Usuario(session.Base):
    __tablename__ = 'usuarios'

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    rol = Column(String)
    is_active = Column(Boolean, nullable=False)

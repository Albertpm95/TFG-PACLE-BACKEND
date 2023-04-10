from __future__ import annotations

from sqlalchemy import Column, Table, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from typing import Set
from db.database import Base
from models.tarea import Tarea


class AlumnosActa(Base):
    __tablename__ = "actas_alumnos"

    id = Column(Integer, primary_key=True)
    idActa = Column(Integer, ForeignKey("actas.idActa"))
    idAlumno = Column(Integer, ForeignKey("alumnos.idAlumno"))


class AlumnosConvocatoria(Base):
    __tablename__: str = "matriculados_convocatoria"

    id = Column(Integer, primary_key=True)
    idConvocatoria = Column(Integer, ForeignKey("convocatorias.idConvocatoria"))
    idAlumno = Column(Integer, ForeignKey("alumnos.idAlumno"))


class ActaCompresion(Base):
    __tablename__ = "actas_compresion"

    id = Column(Integer, primary_key=True)
    idComprension = Column(Integer, ForeignKey("comprension.idComprension"))
    idActa = Column(Integer, ForeignKey("actas.idActa"))


class ActaExpresion(Base):
    __tablename__ = "actas_expresion"

    id = Column(Integer, primary_key=True)
    idExpresion = Column(Integer, ForeignKey("expresion.idExpresion"))
    idActa = Column(Integer, ForeignKey("actas.idActa"))


class Correccion(Base):
    __tablename__ = "correccion"

    idCorreccion = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey("usuarios.idUsuario"))
    idTarea = Column(Integer, ForeignKey("tareas.idTarea"))
    tareas: Mapped[list[Tarea]] = relationship()

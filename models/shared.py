from __future__ import annotations

from sqlalchemy import Column, Table, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from typing import Set
from db.database import Base
from models.tarea import Tarea


class AlumnosActa(Base):
    __tablename__ = "alumnos_acta"

    id = Column(Integer, primary_key=True)
    idActa = Column(Integer, ForeignKey("actas.idActa"))
    idAlumno = Column(Integer, ForeignKey("alumnos.idAlumno"))


"""
class CorrectorCompresion(Base):
    __tablename__ = "corrector_compresion"

    id = Column(Integer, primary_key=True)
    idCorrector = Column(Integer, ForeignKey("usuarios.idUsuario"))
    idComprension = Column(Integer, ForeignKey("comprension.idComprension"))
"""


class ParteExpresion(Base):
    __tablename__ = "parte_expresion"

    idParte = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey("usuarios.idUsuario"))
    idExpresion = Column(Integer, ForeignKey("expresion.idExpresion"))
    idTarea = Column(Integer, ForeignKey("tareas.idTarea"))
    tareas: Mapped[list[Tarea]] = relationship()

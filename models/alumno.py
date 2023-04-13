import datetime
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import Mapped, relationship

from db.database import Base
from models.colectivoUV import ColectivoUV
from models.genero import Genero


class Alumno(Base):
    __tablename__ = "alumnos"

    idAlumno = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    dni = Column(String, unique=True)
    idGenero = Column(Integer, ForeignKey("generos.idGenero"))
    genero: Mapped[Genero] = relationship()
    idColectivoUV = Column(Integer, ForeignKey("colectivoUV.idColectivoUV"))
    colectivoUV: Mapped[ColectivoUV] = relationship()
    email = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    fechaNacimiento = Column(Date, nullable=False)
    pruebaAdaptada = Column(Boolean, nullable=False, default=True)
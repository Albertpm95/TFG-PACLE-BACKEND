from sqlalchemy import Column, ForeignKey, Integer, String
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
    idColectivo = Column(Integer, ForeignKey("colectivoUV.idColectivoUV"))
    colectivo: Mapped[ColectivoUV] = relationship()

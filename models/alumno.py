from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from db.database import Base
from models.acta import Acta
from models.genero import Genero


class Alumno(Base):
    __tablename__ = "alumnos"

    idAlumno = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    dni = Column(String, unique=True)
    idGenero = Column(Integer, ForeignKey("generos.idGenero"))
    genero: Mapped[Genero] = relationship()

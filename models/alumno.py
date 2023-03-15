from sqlalchemy import Column, String, Integer

from db.database import Base


class Alumno(Base):
    __tablename__ = "alumnos"

    idAlumno = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    dni = Column(String, unique=True)

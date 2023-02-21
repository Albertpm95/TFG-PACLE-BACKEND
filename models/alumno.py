from sqlalchemy import Column, ForeignKey, String, Integer

from db.database import Base


class Alumno(Base):
    __tablename__ = "alumnos"

    id_alumno = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    dni = Column(String, unique=True, nullable=False)

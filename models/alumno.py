from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from db.database import Base


class Alumno(Base):
    __tablename__ = "alumnos"

    id_alumno = Column(String, primary_key=True, index=True)
    id_acta = Column(String, ForeignKey("Pacle_db.actas.id_acta"))
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    dni = Column(String, nullable=False)

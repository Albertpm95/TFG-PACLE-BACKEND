from msilib import schema
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from db.database import Base


class Alumno(Base):
    __tablename__ = "alumnos"

    id_alumno = Column(String, primary_key=True, index=True)
    # id_acta = Column(String, ForeignKey("actas"))
    id_acta = relationship("Acta", back_populates="id_alumno")
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    dni = Column(String, nullable=False)

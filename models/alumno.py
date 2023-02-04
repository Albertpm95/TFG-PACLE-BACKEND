from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db.base_class import Base
from models.shared import presentados_acta

class Alumno(Base):
    __tablename__ = 'alumnos'

    id = Column(String, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    examinado_convocatorias = relationship(
        "Acta", secondary=presentados_acta, back_populates=True)

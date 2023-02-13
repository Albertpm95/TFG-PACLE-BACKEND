from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.shared import presentados_acta


class Acta(Base):
    __tablename__ = 'actas'

    id = Column(String, primary_key=True, index=True)
    lenguaje = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    fecha = Column(DateTime, nullable=False)
    presentados = relationship(
        "Alumno", secondary=presentados_acta, back_populates=True)

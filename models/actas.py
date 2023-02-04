from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship

from db.base_class import Base
from models.shared import presentados_acta


class Acta(Base):
    __tablename__ = 'actas'

    id = Column(String, primary_key=True, index=True)
    lenguage = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    fecha = Column(DateTime, nullable=False)
    presentados = relationship(
        "Alumno", secondary=presentados_acta, back_populates=True)

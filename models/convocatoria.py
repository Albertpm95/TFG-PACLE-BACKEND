from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.shared import presentados_acta


class ConvocatoriaBase(Base):
    __tablename__ = 'convocatorias'

    id = Column(String, primary_key=True, index=True)
    lenguaje = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    fecha = Column(DateTime, nullable=False)
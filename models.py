from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text


class Convocatoria(Base):
    __tablename__ = 'items'
    id_convocatoria = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

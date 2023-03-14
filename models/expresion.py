from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, null
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.database import Base


class Expresion(Base):
    __tablename__ = "expresion"

    id_expresion = Column(Integer, primary_key=True, unique=True)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)

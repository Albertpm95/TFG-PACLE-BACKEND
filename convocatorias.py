from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Convocatoria(Base):
    __tablename__ = "convocatorias"

    id_convocatoria = Column(Integer, primary_key=True, index=True)
    name = Column(String)

from sqlalchemy import Column, ForeignKey, Integer
from db.database import Base


class Tarea(Base):
    __tablename__ = "tarea"

    alcance = Column(Integer, nullable=False, default=0)
    coherencia = Column(Integer, nullable=False, default=0)
    correccion = Column(Integer, nullable=False, default=0)
    eficaciac = Column(Integer, nullable=False, default=0)
    id_corrector = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_tarea = Column(Integer, nullable=False, primary_key=True)

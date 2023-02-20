from sqlalchemy import Column, ForeignKey, Integer, String
from db.database import Base


class Tarea(Base):
    __tablename__ = "tarea"

    id_tarea = Column(String, nullable=False, primary_key=True)
    alcance = Column(Integer, nullable=False, default=0)
    coherencia = Column(Integer, nullable=False, default=0)
    correccion = Column(Integer, nullable=False, default=0)
    eficaciac = Column(Integer, nullable=False, default=0)
    id_corrector = Column(String, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_expresion = Column(String, ForeignKey("actas.id_acta"), nullable=False)

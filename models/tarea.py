from sqlalchemy import Column, ForeignKey, Integer, String
from db.base_class import Base


class Tarea(Base):
    __tablename__ = "tarea"

    id_tarea = Column(String, nullable=False, primary_key=True)
    alcance = Column(Integer, nullable=False, default=0)
    coherencia = Column(Integer, nullable=False, default=0)
    correccion = Column(Integer, nullable=False, default=0)
    eficaciac = Column(Integer, nullable=False, default=0)
    id_corrector = Column(String, ForeignKey("Pacle_db.usuarios.id_usuario"), nullable=False)
    id_expresion = Column(String, ForeignKey("Pacle_db.actas.id_acta"), nullable=False)

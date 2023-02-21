from sqlalchemy import Column, DateTime, ForeignKey, Integer

from db.database import Base


class Acta(Base):
    __tablename__ = "actas"

    fecha = Column(DateTime, nullable=False)
    id_acta = Column(Integer, primary_key=True, index=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id_alumno"))
    id_comprension_auditiva = Column(Integer, ForeignKey("comprension.id_comprension"))
    id_comprension_lectora = Column(Integer, ForeignKey("comprension.id_comprension"))
    id_convocatoria = Column(Integer, ForeignKey("convocatorias.id_convocatoria"))
    id_expresion = Column(Integer, ForeignKey("expresion.id_expresion"))
    id_expresion_oral = Column(Integer, ForeignKey("expresion.id_expresion"))

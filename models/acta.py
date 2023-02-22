from sqlalchemy import Column, DateTime, ForeignKey, Integer

from db.database import Base


class Acta(Base):
    __tablename__ = "actas"

    id_convocatoria = Column(Integer, ForeignKey("convocatorias.id_convocatoria"))
    fecha = Column(DateTime, nullable=False)
    id_acta = Column(Integer, primary_key=True, index=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id_alumno"))
    expresion_escrita = Column(Integer, ForeignKey("expresion.id_expresion"))
    expresion_oral = Column(Integer, ForeignKey("expresion.id_expresion"))
    comprension_lectiva = Column(Integer, ForeignKey("comprension.id_comprension"))
    comprension_auditiva = Column(Integer, ForeignKey("comprension.id_comprension"))

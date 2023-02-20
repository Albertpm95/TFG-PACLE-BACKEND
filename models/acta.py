from sqlalchemy import Column, DateTime, ForeignKey, String

from db.database import Base


class Acta(Base):
    __tablename__ = "actas"

    comprension_auditiva = Column(
        String, ForeignKey("comprension.id_comprension"), nullable=False
    )
    comprension_lectora = Column(
        String, ForeignKey("comprension.id_comprension"), nullable=False
    )
    expresion_escrita = Column(
        String, ForeignKey("expresion.id_comprension"), nullable=False
    )
    expresion_oral = Column(
        String, ForeignKey("expresion.id_comprension"), nullable=False
    )
    fecha = Column(DateTime, nullable=False)
    id_acta = Column(String, primary_key=True)
    id_alumno = Column(String, ForeignKey("alumnos.id_alumnos"))
    id_convocatoria = Column(String, ForeignKey("convocatorias.id_convocatoria"))

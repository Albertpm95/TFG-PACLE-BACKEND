from colorama import Fore
from sqlalchemy import Column, DateTime, ForeignKey, Integer


from db.database import Base


class Acta(Base):
    __tablename__ = "actas"

    id_convocatoria = Column(Integer, ForeignKey("convocatorias.id_convocatoria"))
    fecha = Column(DateTime, nullable=False)
    id_acta = Column(Integer, primary_key=True, index=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id_alumno"))
    id_expresion_escrita = Column(
        Integer, ForeignKey("expresion_escrita.id_expresion_escrita")
    )
    id_expresion_oral = Column(
        Integer, ForeignKey("expresion_escrita.id_expresion_escrita")
    )
    id_comprension_auditiva = Column(
        Integer, ForeignKey("comprension_auditiva.id_comprension_auditiva")
    )
    id_comprension_lectiva = Column(
        Integer, ForeignKey("comprension_lectiva.id_comprension_lectiva")
    )

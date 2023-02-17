from datetime import date, datetime
from psycopg2 import Date
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Acta(Base):
    __tablename__ = "actas"

    comprension_auditiva = Column(
        String, ForeignKey("Pacle_db.comprension.id_comprension"), nullable=False
    )
    comprension_lectora = Column(
        String, ForeignKey("Pacle_db.comprension.id_comprension"), nullable=False
    )
    expresion_escrita = Column(
        String, ForeignKey("Pacle_db.expresion.id_comprension"), nullable=False
    )
    expresion_oral = Column(
        String, ForeignKey("Pacle_db.expresion.id_comprension"), nullable=False
    )
    fecha = Column(DateTime, nullable=False)
    id_acta = Column(String, ForeignKey("Pacle_db.actas.id_acta"))
    id_alumno = Column(String, primary_key=True, index=True)
    id_convocatoria = Column(
        String, ForeignKey("Pacle_db.convocatorias.id_convocatoria")
    )
    nombre = Column(String, nullable=False)

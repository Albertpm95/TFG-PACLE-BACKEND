from sqlalchemy import Column, ForeignKey, Table
from db.base_class import Base

presentados_acta = Table(
    "presentados_acta",
    Base.metadata,
    Column("id_alumno", ForeignKey("alumnos.id"), primary_key=True),
    Column("id_acta", ForeignKey("actas.id"), primary_key=True)
)

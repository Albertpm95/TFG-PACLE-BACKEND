from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from db.database import Base


alumnos_acta = Table(
    "alumnos_acta",
    Base.metadata,
    Column("idActa", ForeignKey("actas.idActa"), primary_key=True),
    Column("idAlumno", ForeignKey("alumnos.idAlumno"), primary_key=True),
)

correctores_auditiva = Table(
    "correctores_auditiva",
    Base.metadata,
    Column("idUsuario", ForeignKey("usuarios.idUsuario")),
    Column("idComprensionAuditiva", ForeignKey("comprension_auditiva.idComprension")),
)

correctores_lectora = Table(
    "correctores_lectora",
    Base.metadata,
    Column("idUsuario", ForeignKey("usuarios.idUsuario")),
    Column("idComprensionLectora", ForeignKey("comprension_lectora.idComprension")),
)

from fastapi import Query, HTTPException
from sqlalchemy.orm import Session

from models.comprension_auditiva import ComprensionAuditiva as mod_comprension_auditiva
from models.comprension_lectora import ComprensionLectora as mod_comprensionLectora


def get_comprension_auditiva(id_comprension: int, db: Session):
    return db.query(mod_comprension_auditiva).filter(
        mod_comprension_auditiva.id_comprension == id_comprension,
    )


def get_comprension_lectiva(id_comprension: int, db: Session):
    return db.query(mod_comprensionLectora).filter(
        mod_comprensionLectora.id_comprension == id_comprension,
    )

from fastapi import Query, HTTPException
from sqlalchemy.orm import Session

from models.comprension_auditiva import ComprensionAuditiva as mod_comprension_auditiva
from models.comprension_lectora import ComprensionLectora as mod_comprension_lectora


def get_compresion_auditiva(id_compresion: int, db: Session):
    return db.query(mod_comprension_auditiva).filter(
        mod_comprension_auditiva.id_comprension == id_compresion,
    )


def get_compresion_lectiva(id_compresion: int, db: Session):
    return db.query(mod_comprension_lectora).filter(
        mod_comprension_lectora.id_comprension == id_compresion,
    )

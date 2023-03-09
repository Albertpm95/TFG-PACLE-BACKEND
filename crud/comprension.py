from fastapi import Query, HTTPException
from sqlalchemy.orm import Session

from models import comprension as mod_comprension


def get_compresion_auditiva(id_compresion: int, db: Session):
    return db.query(mod_comprension).filter(
        mod_comprension.Comprension.tipo == "auditiva",
        mod_comprension.Comprension.id_comprension == id_compresion,
    )


def get_compresion_lectiva(id_compresion: int, db: Session):
    return db.query(mod_comprension).filter(
        mod_comprension.Comprension.tipo == "lectiva",
        mod_comprension.Comprension.id_comprension == id_compresion,
    )

from fastapi import Query, HTTPException
from sqlalchemy.orm import Session

from models.comprension import Comprension as mod_comprension


def get_comprension_auditiva(id_comprension: int, db: Session):
    return db.query(mod_comprension).filter(
        mod_comprension.id_comprension == id_comprension,
    )


def get_comprension_lectiva(id_comprension: int, db: Session):
    return db.query(mod_comprension).filter(
        mod_comprension.id_comprension == id_comprension,
    )

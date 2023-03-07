from fastapi import Query, HTTPException
from sqlalchemy.orm import Session

from models import comprension as mod_comprension


def get_expresion_auditiva(id_acta: int, db: Session):
    return db.query(mod_comprension).filter(
        mod_comprension.Comprension.tipo == "auditiva",
        mod_comprension.Comprension.id_acta == id_acta,
    )


def get_expresion_lectiva(id_acta: int, db: Session):
    return db.query(mod_comprension).filter(
        mod_comprension.Comprension.tipo == "lectiva",
        mod_comprension.Comprension.id_acta == id_acta,
    )

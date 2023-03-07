from fastapi import Query, HTTPException
from sqlalchemy.orm import Session

from models import expresion as mod_expresion


def get_expresion_escrita(id_acta: int, db: Session):
    return db.query(mod_expresion).filter(
        mod_expresion.Expresion.tipo == "escrita",
        mod_expresion.Expresion.id_acta == id_acta,
    )


def get_expresion_oral(id_acta: int, db: Session):
    return db.query(mod_expresion).filter(
        mod_expresion.Expresion.tipo == "oral",
        mod_expresion.Expresion.id_acta == id_acta,
    )

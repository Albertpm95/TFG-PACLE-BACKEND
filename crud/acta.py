from fastapi import Query
from sqlalchemy.orm import Session

from models import acta as mod_acta

""" CRUD Principal """


def get_convocatorias(db: Session):
    return db.query(mod_acta.Acta).all()


def get_convocatoria_id(id_convocatoria: str, db: Session):
    return db.query(mod_acta.Acta).filter(
        mod_acta.Acta.id_convocatoria == id_convocatoria
    )

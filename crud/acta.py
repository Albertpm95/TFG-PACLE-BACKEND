from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import acta as mod_acta

""" CRUD Principal """


def get_convocatorias(db: Session):
    convocatorias = db.query(mod_acta.Acta).all()
    if not convocatorias:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido recuperar la lista de convocatorias o esta vacia.",
        )
    return convocatorias


def get_convocatoria_id(id_convocatoria: str, db: Session):
    return db.query(mod_acta.Acta).filter(
        mod_acta.Acta.id_convocatoria == id_convocatoria
    )

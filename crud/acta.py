from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import acta as mod_acta
from schemas.acta import ActaBase

from crud import convocatoria as crud_convocatoria
from crud import alumno as crud_alumno

""" CRUD Principal """


def create_acta(db: Session, acta: ActaBase):
    existe_convocatoria = crud_convocatoria.get_convocatoria_id(
        db=db, id_convocatoria=acta.convocatoria.id_convocatoria
    )
    if not existe_convocatoria:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido crear el acta, no existe la convocatoria.",
        )

    existe_alumno = crud_alumno.get_alumno_id(acta.alumno.id_alumno, db=db)
    if not existe_alumno:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido crear el acta, no existe el alumno.",
        )


def get_convocatorias(db: Session):
    return db.query(mod_acta.Acta).all()


def get_convocatoria_id(id_convocatoria: int, db: Session):
    return db.query(mod_acta.Acta).filter(
        mod_acta.Acta.id_convocatoria == id_convocatoria
    )


def existe_acta_alumno_convocatoria(id_convocatoria: int, id_alumno: int, db: Session):
    return db.query(mod_acta.Acta).filter(
        mod_acta.Acta.id_convocatoria == id_convocatoria,
        mod_acta.Acta.id_alumno == id_alumno,
    )

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import acta as mod_acta
from schemas.acta import Acta

from crud import convocatoria as crud_convocatoria
from crud import alumno as crud_alumno
from crud import usuario as crud_usuario
from crud import expresion as crud_expresion
from crud import comprension as crud_comprension

""" CRUD Principal """


def create_acta(db: Session, acta: Acta):
    """
      existe_convocatoria = crud_convocatoria.get_convocatoria_id(
        db=db, id_convocatoria=acta.convocatoria.id_convocatoria
    )
    if not existe_convocatoria:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido crear el acta, no existe .",
        )
    existe_alumno = crud_alumno.get_alumno_id(acta.alumno.id_alumno, db=db)
    if not existe_alumno:

    existe_expresion_escrita = crud_expresion.get_expresion_escrita(acta.id_acta, db=db)
    if not existe_expresion_escrita:

    existe_expresion_oral = crud_expresion
    if not existe_expresion_oral:

    existe_comprension_lectora = crud_comprension
    if not existe_comprension_lectora:

    existe_comprension_auditiva = crud_comprension
    if not existe_comprension_auditiva:
    """


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

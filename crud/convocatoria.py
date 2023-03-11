from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.convocatoria import Convocatoria as mod_convocatoria
from schemas.convocatoria import Convocatoria as sch_convocatoria
from schemas.convocatoria import ConvocatoriaDB as sch_convocatoria_DB

from crud import lenguaje as crud_idioma
from crud import horario as crud_horario

""" CRUD PRINCIPAL """


def get_convocatorias(db: Session):
    convocatorias = db.query(mod_convocatoria).all()
    return convocatorias


def get_convocatorias_activas(db: Session):
    return db.query(mod_convocatoria).filter_by(estado=True).all()


def get_convocatoria_id(id_convocatoria: int, db: Session):
    convocatoria = (
        db.query(mod_convocatoria)
        .filter(mod_convocatoria.id_convocatoria == id_convocatoria)
        .first()
    )
    if not convocatoria:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra la convocatoria seleccionada.",
        )
    return convocatoria


def create_convocatoria(convocatoria: sch_convocatoria, db: Session):
    existe_lenguaje = crud_idioma.get_idioma_id(db, convocatoria.lenguaje.id_lenguaje)
    if not existe_lenguaje:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el lenguaje seleccionado, no se ha podido crear la convocatoria.",
        )
    existe_horario = crud_horario.get_horario_id(
        db, id_horario=convocatoria.horario.id_horario
    )
    if not existe_horario:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el horario seleccionado, no se ha podido crear la convocatoria.",
        )

    db_convocatoria = mod_convocatoria(
        comprension_auditiva_puntuacion_maxima_parte=convocatoria.comprension_auditiva_puntuacion_maxima_parte,
        comprension_lectora_puntuacion_maxima_parte=convocatoria.comprension_lectora_puntuacion_maxima_parte,
        expresion_escrita_puntuacion_maxima_parte=convocatoria.expresion_escrita_puntuacion_maxima_parte,
        expresion_oral_puntuacion_maxima_parte=convocatoria.expresion_oral_puntuacion_maxima_parte,
        estado=True,
        fecha=convocatoria.fecha,
        lenguaje=existe_lenguaje,
        horario=existe_horario,
    )
    db.add(db_convocatoria)
    db.commit()
    db.refresh(db_convocatoria)
    return db_convocatoria


def update_convocatoria(convocatoria: sch_convocatoria_DB, db: Session):
    existe_lenguaje = crud_idioma.get_idioma_id(db, convocatoria.lenguaje.id_lenguaje)
    if not existe_lenguaje:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el lenguaje seleccionado, no se ha podido crear la convocatoria.",
        )
    existe_horario = crud_horario.get_horario_id(
        db, id_horario=convocatoria.horario.id_horario
    )
    if not existe_horario:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el horario seleccionado, no se ha podido crear la convocatoria.",
        )
    db_convocatoria = mod_convocatoria(convocatoria)
    db.add(db_convocatoria)
    db.commit()
    db.refresh(db_convocatoria)
    return db_convocatoria

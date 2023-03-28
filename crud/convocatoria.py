from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.convocatoria import Convocatoria as mod_convocatoria
from schemas.convocatoria import Convocatoria as sch_convocatoria
from schemas.convocatoria import ConvocatoriaDB as sch_convocatoria_DB

from crud import lenguaje as crud_idioma
from crud import horario as crud_horario
from crud import nivel as crud_nivel

""" CRUD PRINCIPAL """


def get_convocatorias(db: Session):
    convocatorias = db.query(mod_convocatoria).all()
    return convocatorias


def get_convocatorias_activas(db: Session):
    return db.query(mod_convocatoria).filter_by(estado=True).all()


def get_convocatoria_id(idConvocatoria: int, db: Session):
    convocatoria = (
        db.query(mod_convocatoria)
        .filter(mod_convocatoria.idConvocatoria == idConvocatoria)
        .first()
    )
    if not convocatoria:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra la convocatoria seleccionada.",
        )
    return convocatoria


def create_convocatoria(convocatoria: sch_convocatoria, db: Session):
    existe_lenguaje = crud_idioma.get_idioma_id(db, convocatoria.lenguaje.idLenguaje)
    if not existe_lenguaje:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el lenguaje seleccionado, no se ha podido crear la convocatoria.",
        )
    existe_horario = crud_horario.get_horario_id(
        db, idHorario=convocatoria.horario.idHorario
    )
    if not existe_horario:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el horario seleccionado, no se ha podido crear la convocatoria.",
        )

    existe_nivel = crud_nivel.get_nivel_id(db, convocatoria.nivel.idNivel)
    if not existe_nivel:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el nivel seleccionado, no se ha podido crear la convocatoria.",
        )

    db_convocatoria = mod_convocatoria(
        maxComprensionAuditiva=convocatoria.maxComprensionAuditiva,
        maxComprensionLectora=convocatoria.maxComprensionLectora,
        maxExpresionEscrita=convocatoria.maxExpresionEscrita,
        maxExpresionOral=convocatoria.maxExpresionOral,
        estado=True,
        fecha=convocatoria.fecha,
        lenguaje=existe_lenguaje,
        horario=existe_horario,
        nivel=existe_nivel,
    )
    db.add(db_convocatoria)
    db.commit()
    db.refresh(db_convocatoria)
    return db_convocatoria


def update_convocatoria(convocatoria: sch_convocatoria_DB, db: Session):
    existe_lenguaje = crud_idioma.get_idioma_id(db, convocatoria.lenguaje.idLenguaje)
    if not existe_lenguaje:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el lenguaje seleccionado, no se ha podido crear la convocatoria.",
        )
    existe_horario = crud_horario.get_horario_id(
        db, idHorario=convocatoria.horario.idHorario
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

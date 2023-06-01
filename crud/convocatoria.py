import json
from textwrap import indent

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from crud import horario as crud_horario
from crud import lenguaje as crud_idioma
from crud import nivel as crud_nivel
from crud import parte as crud_parte
from models.convocatoria import Convocatoria
from models.shared import AlumnosConvocatoria as mod_alumnoConvocatoria
from schemas.convocatoria import ConvocatoriaDB as sch_convocatoria_DB
from schemas.convocatoria import ConvocatoriaNueva as sch_convocatoria

""" CRUD PRINCIPAL """


def get_convocatorias(db: Session):
    return db.query(Convocatoria).all()


def get_convocatorias_activas(db: Session):
    return db.query(Convocatoria).filter_by(estado=True).all()


def get_convocatorias_alumno(db: Session, idAlumno: int):
    return db.query(mod_alumnoConvocatoria).filter(mod_alumnoConvocatoria.idAlumno == idAlumno).all()


def get_convocatoria_id(idConvocatoria: int, db: Session):
    convocatoria = db.query(Convocatoria).filter(Convocatoria.idConvocatoria == idConvocatoria).first()
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
    existe_horario = crud_horario.get_horario_id(db, idHorario=convocatoria.horario.idHorario)
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
    existe_convocatoria = existe_convocatoria_specific_identifier(db, convocatoria.specificIdentifier)
    if existe_convocatoria:
        raise HTTPException(
            status_code=404,
            detail="Ya existe una convocatoria con ese identificador.",
        )
    comprensionAuditivaDB = crud_parte.create_parte(convocatoria.parteComprensionAuditiva, db)
    comprensionLectoraDB = crud_parte.create_parte(convocatoria.parteComprensionLectora, db)
    expresionEscritaDB = crud_parte.create_parte(convocatoria.parteExpresionEscrita, db)
    expresionOralDB = crud_parte.create_parte(convocatoria.parteExpresionOral, db)
    db_convocatoria = Convocatoria(
        estado=True,
        fecha=convocatoria.fecha,
        lenguaje=existe_lenguaje,
        horario=existe_horario,
        nivel=existe_nivel,
        specificIdentifier=convocatoria.specificIdentifier,
        parteComprensionAuditiva=comprensionAuditivaDB,
        parteComprensionLectora=comprensionLectoraDB,
        parteExpresionEscrita=expresionEscritaDB,
        parteExpresionOral=expresionOralDB
    )
    db.add(db_convocatoria)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="No se ha podido crear la convocatoria.")
    db.refresh(db_convocatoria)
    return db_convocatoria


def update_convocatoria(convocatoria_update: sch_convocatoria_DB, db: Session):
    existe_convocatoria = get_convocatoria_id(db=db, idConvocatoria=convocatoria_update.idConvocatoria)
    if not existe_convocatoria:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra la convocatoria seleccionada, no se ha podido actualizar.",
        )
    existe_lenguaje = crud_idioma.get_idioma_id(db, convocatoria_update.lenguaje.idLenguaje)
    if not existe_lenguaje:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el lenguaje seleccionado, no se ha podido actualizar la convocatoria.",
        )
    existe_horario = crud_horario.get_horario_id(db, idHorario=convocatoria_update.horario.idHorario)
    if not existe_horario:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el horario seleccionado, no se ha podido actualizar la convocatoria.",
        )
    existe_nivel = crud_nivel.get_nivel_id(db, convocatoria_update.nivel.idNivel)
    if not existe_nivel:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el nivel seleccionado, no se ha podido actualizar la convocatoria.",
        )
    existe_convocatoria.idConvocatoria = convocatoria_update.idConvocatoria
    existe_convocatoria.estado = convocatoria_update.estado
    existe_convocatoria.fecha = convocatoria_update.fecha
    existe_convocatoria.horario = existe_horario
    existe_convocatoria.nivel = existe_nivel
    existe_convocatoria.lenguaje = existe_lenguaje
    existe_convocatoria.specificIdentifier = convocatoria_update.specificIdentifier
    existe_convocatoria.parteComprensionAuditiva = crud_parte.update_parte(
        db=db, parte=convocatoria_update.parteComprensionAuditiva
    )
    existe_convocatoria.parteComprensionLectora = crud_parte.update_parte(
        db=db, parte=convocatoria_update.parteComprensionLectora
    )
    existe_convocatoria.parteExpresionEscrita = crud_parte.update_parte(
        db=db, parte=convocatoria_update.parteExpresionEscrita
    )
    existe_convocatoria.parteExpresionOral = crud_parte.update_parte(
        db=db, parte=convocatoria_update.parteExpresionOral
    )
    db.commit()
    db.refresh(existe_convocatoria)
    return existe_convocatoria


def existe_convocatoria_specific_identifier(db: Session, specificIdentifier: str):
    return db.query(Convocatoria).filter(Convocatoria.specificIdentifier == specificIdentifier).first()


def delete_convocatoria(db: Session, idConvocatoria: int):
    existe_convocatoria: Convocatoria = get_convocatoria_id(db=db, idConvocatoria=idConvocatoria)
    if not existe_convocatoria:
        raise HTTPException(status_code=404, detail="No existe esa convocatoria, no puede borrarse.")
    db.delete(existe_convocatoria)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="No se puede borrar la convocatoria porque esta siendo referenfciada."
        )

    return {"Borrado": "Borrada la convocatoria."}

from fastapi import Query, HTTPException
from sqlalchemy.orm import Session

from schemas.expresion_escrita import ExpresionEscrita as sch_expresion_escrita
from schemas.expresion_oral import ExpresionOral as sch_expresion_oral
from models.expresion_escrita import ExpresionEscrita as mod_expresion_escrita
from models.expresion_oral import ExpresionOral as mod_expresion_oral

from crud import tarea as crud_tarea


def get_expresion_escrita(id_expresion: int, db: Session):
    return (
        db.query(mod_expresion_escrita)
        .filter(mod_expresion_escrita.id_expresion == id_expresion)
        .first()
    )


def create_expresion_escrita(expresion_nueva: sch_expresion_escrita, db: Session):
    nueva_tarea_1 = crud_tarea.create_tarea(expresion_nueva.tarea_1, db)
    nueva_tarea_2 = crud_tarea.create_tarea(expresion_nueva.tarea_2, db)
    expresion_db = mod_expresion_escrita(
        observaciones=expresion_nueva.observaciones,
        porcentaje=expresion_nueva.porcentaje,
        puntos_conseguidos=expresion_nueva.puntos_conseguidos,
        puntuacion_maxima_parte=expresion_nueva.puntuacion_maxima_parte,
        tarea_1=nueva_tarea_1,
        tarea_2=nueva_tarea_2,
    )
    db.add(expresion_db)
    db.commit()
    db.refresh(expresion_db)
    return expresion_db


def get_expresion_oral(id_expresion: int, db: Session):
    return (
        db.query(mod_expresion_oral)
        .filter(mod_expresion_oral.id_expresion == id_expresion)
        .first()
    )


def create_expresion_oral(expresion_nueva: sch_expresion_oral, db: Session):
    nueva_tarea_1 = crud_tarea.create_tarea(expresion_nueva.tarea_1, db)
    nueva_tarea_2 = crud_tarea.create_tarea(expresion_nueva.tarea_2, db)
    expresion_db = mod_expresion_oral(
        observaciones=expresion_nueva.observaciones,
        porcentaje=expresion_nueva.porcentaje,
        puntos_conseguidos=expresion_nueva.puntos_conseguidos,
        puntuacion_maxima_parte=expresion_nueva.puntuacion_maxima_parte,
        tarea_1=nueva_tarea_1,
        tarea_2=nueva_tarea_2,
    )
    db.add(expresion_db)
    db.commit()
    db.refresh(expresion_db)
    return expresion_db

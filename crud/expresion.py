from fastapi import Query, HTTPException
from sqlalchemy.orm import Session

from schemas.expresion import Expresion as sch_expresion
from models.expresion import Expresion as mod_expresion

from crud import tarea as crud_tarea

from fakeDB import expresionOral, expresionEscrita


def get_expresionEscrita(id_expresion: int, db: Session):
    return expresionEscrita
    return (
        db.query(mod_expresion())
        .filter(mod_expresion.id_expresion == id_expresion)
        .first()
    )


def create_expresion(expresion_nueva: sch_expresion, db: Session):
    return expresionEscrita
    expresion_db = mod_expresion(
        observaciones=expresion_nueva.observaciones,
        porcentaje=expresion_nueva.porcentaje,
        puntosConseguidos=expresion_nueva.puntosConseguidos,
        puntuacionMaxima=expresion_nueva.puntuacionMaxima,
        tipo=expresion_nueva.tipo,
    )
    # db.add(expresion_db)
    # db.commit()
    # db.refresh(expresion_db)
    return expresion_db


def get_expresion_oral(id_expresion: int, db: Session):
    return expresionOral
    return (
        db.query(mod_expresion)
        .filter(mod_expresion.id_expresion == id_expresion)
        .filter(mod_expresion.tipo == "oral")
        .first()
    )


def create_expresion_oral(expresion_nueva: sch_expresion, db: Session):
    return expresionOral
    nueva_tarea_1 = crud_tarea.create_tarea(expresion_nueva.tarea_1, db)
    nueva_tarea_2 = crud_tarea.create_tarea(expresion_nueva.tarea_2, db)
    expresion_db = mod_expresion_oral(
        observaciones=expresion_nueva.observaciones,
        porcentaje=expresion_nueva.porcentaje,
        puntosConseguidos=expresion_nueva.puntosConseguidos,
        puntuacionMaxima=expresion_nueva.puntuacionMaxima,
        tarea_1=nueva_tarea_1,
        tarea_2=nueva_tarea_2,
    )
    db.add(expresion_db)
    db.commit()
    db.refresh(expresion_db)
    return expresion_db

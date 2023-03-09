from fastapi import Query, HTTPException
from sqlalchemy.orm import Session

from schemas.expresion import Expresion as sch_Expresion
from models.expresion import Expresion as mod_expresion

from crud import tarea as crud_tarea


def get_expresion_escrita(id_expresion: int, db: Session):
    return db.query(mod_expresion).filter(
        mod_expresion.tipo == "escrita",
        mod_expresion.id_expresion == id_expresion,
    )


def create_expresion(expresion_nueva: sch_Expresion, db: Session):
    nueva_tarea_1 = crud_tarea.create_tarea(expresion_nueva.tarea_1, db)
    nueva_tarea_2 = crud_tarea.create_tarea(expresion_nueva.tarea_2, db)
    expresion_db = mod_expresion(
        tipo=expresion_nueva.tipo,
        observaciones=expresion_nueva.observaciones,
        porcentaje=expresion_nueva.pocentaje,
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
    return db.query(mod_expresion).filter(
        mod_expresion.tipo == "oral", mod_expresion.id_expresion == id_expresion
    )

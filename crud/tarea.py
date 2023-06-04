import json

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.tarea import Correccion as mod_correccion
from models.tarea import Tarea as mod_tarea
from models.tarea import TareaCorregida as mod_tareaCorregida
from schemas.correccion import Correccion as sch_correccion
from schemas.tarea import Tarea as sch_tarea
from schemas.tarea import TareaCorregida as sch_tareaCorregida
from schemas.tarea import TareaCorregidaDB as sch_tareaCorregidaDB
from schemas.tarea import TareaDB as sch_tareaDB


def get_tarea_id(idTarea: int, db: Session):
    return db.query(mod_tarea).filter(mod_tarea.idTarea == idTarea).first()

def get_tarea_parte_name(nombreTarea: str, db: Session):
    return db.query(mod_tarea).filter(mod_tarea.nombreTarea == nombreTarea).first()

def get_tarea_parte_name_corregida(nombreTarea: str, db: Session):
    return db.query(mod_tareaCorregida).filter(mod_tareaCorregida.nombreTarea == nombreTarea).first()

def get_tareas_parte(idParte: int, db: Session):
    return db.query(mod_tarea).filter(mod_tarea.idParte == idParte).all()


def create_tarea(tarea: sch_tarea, db: Session):
    tarea_db = mod_tarea(nombreTarea=tarea.nombreTarea)
    db.add(tarea_db)
    db.flush()
    db.refresh(tarea_db)
    return tarea_db


def create_tareas(tareas: list[sch_tarea], db: Session):
    tareasDB = []
    for tarea in tareas:
        existe_tarea = get_tarea_parte_name(tarea.nombreTarea, db)
        if existe_tarea:
            tareasDB.append(update_tarea(existe_tarea, db))
        if not existe_tarea:
            tareasDB.append(create_tarea(tarea, db))
    return tareasDB


def create_tarea_corregida(tareaCorregida: sch_tareaCorregida, db: Session):
    existe_tarea = get_tarea_id(tareaCorregida.idTarea, db)
    if existe_tarea:
        tareaCorregida_db = mod_tareaCorregida(tarea=existe_tarea, puntuacion=tareaCorregida.puntuacion)
    db.add(tareaCorregida_db)
    db.refresh(tareaCorregida_db)
    return tareaCorregida_db


def create_tareas_corregidas(tareas: list[sch_tareaCorregida], db: Session):
    tareasCorregidasDB = []
    for tarea in tareas:
        existe_tarea = get_tarea_id(tarea.idTarea, db)
        if existe_tarea:
            tareasCorregidasDB.append(update_tarea_corregida(existe_tarea, db))
        if not existe_tarea:
            tareasCorregidasDB.append(create_tarea_corregida(tarea, db))
    return tareasCorregidasDB


async def create_correccion(correccion: sch_correccion, db: Session):
    tareasCorregidasDB = create_tareas_corregidas(correccion.tareas, db)
    db_correccion = mod_correccion(
        corrector=correccion.corrector,
        tareasCorregidas=tareasCorregidasDB,
    )
    db.add(db_correccion)
    db.refresh(db_correccion)
    return db_correccion


def update_tarea(tarea: sch_tareaDB, db: Session):
    tarea_db = get_tarea_id(tarea.idTarea, db)
    tarea_db.nombreTarea = tarea.nombreTarea
    db.refresh(tarea_db)
    return tarea_db

def update_tarea_corregida(tarea: sch_tareaCorregidaDB, db: Session):
    tarea_db = get_tarea_id(tarea.idTarea, db)
    tarea_db.puntuacion = tarea.puntuacion
    db.refresh(tarea_db)
    return tarea_db

def delete_tarea(db: Session, idTarea: int):
    existe_tarea: mod_tarea = get_tarea_id(db, idTarea)
    if existe_tarea:
        db.delete(existe_tarea)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()


def delete_tareas(db: Session, idParte: int):
    tareas_a_borrar = get_tareas_parte(idParte=idParte, db=db)

    for tarea in tareas_a_borrar:
        delete_tarea(db, tarea.idTarea)

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.tarea import Tarea as mod_tarea
from schemas.tarea import Tarea as sch_tarea
from schemas.tarea import TareaDB as sch_tareaDB


def get_tarea_id(idTarea, db: Session):
    return db.query(mod_tarea).filter(mod_tarea.idTarea == idTarea).first()

def get_tarea_parte_name(nombreTarea: str, db: Session):
    return db.query(mod_tarea).filter(mod_tarea.nombreTarea == nombreTarea).first()

def create_tarea(tarea: sch_tarea,  db: Session):
    existe_tarea = get_tarea_parte_name(tarea.nombreTarea, db)
    if not existe_tarea:
        tarea_db = mod_tarea(nombreTarea=tarea.nombreTarea)
        db.add(tarea_db)
        db.commit()
        db.refresh(tarea_db)
        return tarea_db

def update_tarea(tarea: sch_tareaDB, db: Session):
    tarea_db = mod_tarea(
        nombre_tarea=tarea.nombreTarea, idTarea=tarea.idTarea
    )
    db.commit()
    db.refresh(tarea_db)
    return tarea_db

def create_tareas(tareas: list[sch_tarea], db: Session):
    tareasDB = []
    for tarea in tareas:
        tareasDB.append(create_tarea(tarea,  db))
    return tareasDB

def delete_tarea(db: Session, idTarea: int):
    existe_tarea: mod_tarea = get_tarea_id(db, idTarea)
    if existe_tarea:
        db.delete(existe_tarea)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
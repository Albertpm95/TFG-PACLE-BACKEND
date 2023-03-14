from sqlalchemy.orm import Session

from schemas.tarea import Tarea as sch_tarea
from schemas.tarea import TareaDB as sch_tareaDB
from models.tarea import Tarea as mod_tarea


def get_tarea_id(id_tarea, db: Session):
    return db.query(mod_tarea).filter(mod_tarea.id_tarea == id_tarea)


def get_tareas_corrector(id_corrector, db: Session):
    return db.query(mod_tarea).filter(mod_tarea.id_corrector == id_corrector)


def create_tarea(tarea: sch_tarea, db: Session):
    tarea_db = mod_tarea(valor=tarea.valor, nombre_tarea=tarea.nombre_tarea)
    db.add(tarea_db)
    db.commit()
    db.refresh(tarea_db)
    return tarea_db


def update_tarea(tarea: sch_tareaDB, db: Session):
    tarea_db = mod_tarea(
        valor=tarea.valor, nombre_tarea=tarea.nombre_tarea, id_tarea=tarea.id_tarea
    )
    db.add(tarea_db)
    db.commit()
    db.refresh(tarea_db)
    return tarea_db

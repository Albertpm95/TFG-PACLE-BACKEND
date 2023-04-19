from sqlalchemy.orm import Session

from schemas.tarea import Tarea as sch_tarea
from schemas.tarea import TareaDB as sch_tareaDB
from models.tarea import Tarea as mod_tarea


def get_tarea_id(idTarea, db: Session):
    return db.query(mod_tarea).filter(mod_tarea.idTarea == idTarea)

def create_tarea(tarea: sch_tarea, idParte: int, db: Session):
    tarea_db = mod_tarea(nombreTarea=tarea.nombreTarea, idParte=idParte)
    db.add(tarea_db)
    db.commit()
    db.refresh(tarea_db)
    return tarea_db

def create_tareas(tareas: list[sch_tarea], idParte: int, db: Session):
    tareasDB = []
    for tarea in tareas:
        tareasDB.append(create_tarea(tarea, idParte, db))
    print('Tareas creadas: ', tareasDB)
    return tareasDB

def update_tarea(tarea: sch_tareaDB, db: Session):
    tarea_db = mod_tarea(
        nombre_tarea=tarea.nombreTarea, idTarea=tarea.idTarea
    )
    db.add(tarea_db)
    db.commit()
    db.refresh(tarea_db)
    return tarea_db

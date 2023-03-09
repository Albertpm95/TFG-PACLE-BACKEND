from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.tarea import Tarea as sch_tarea
from models.tarea import Tarea as mod_tarea

from crud import usuario as crud_usuario


def get_tarea_id(id_tarea, db: Session):
    return db.query(mod_tarea).filter(mod_tarea.id_tarea == id_tarea)


def get_tareas_corrector(id_corrector, db: Session):
    return db.query(mod_tarea).filter(mod_tarea.id_corrector == id_corrector)


def create_tarea(tarea: sch_tarea, db: Session):
    existe_corrector = crud_usuario.get_rol_id(db, tarea.corrector.id_usuario)
    if not existe_corrector:
        raise HTTPException(status_code=404, detail="No existe el corrector.")
    tarea_db = mod_tarea(
        alcance=tarea.alcance,
        coherencia=tarea.coherencia,
        correccion=tarea.correccion,
        eficaciac=tarea.eficaciaC,
        corrector=tarea.corrector,
    )

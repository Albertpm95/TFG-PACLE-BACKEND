from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.parte import Parte
from schemas.parte import ParteBase

from crud import tarea as crud_tarea

def create_parte(parte: ParteBase, db: Session):
    parte_db = Parte(
        puntuacionMaxima=parte.puntuacionMaxima,
        tipo=parte.tipo,
        tareas=[]
    )
    db.add(parte_db)
    db.commit()
    db.refresh(parte_db)
    return parte_db

def get_parte_id(idParte: int, db: Session):
    return db.query(Parte).filter(Parte.idParte == idParte).first()

def delete_parte(db: Session, idParte: int):
    existe_parte: Parte = get_parte_id(db, idParte)
    if not existe_parte:
        raise HTTPException(
            status_code=404, detail="No existe ese genero, no puede borrarse."
        )
    db.delete(existe_parte)

    try:
        db.commit()
    except IntegrityError:
        db.partelback()
        raise HTTPException(status_code=400, detail="Cannot delete row due to foreign key constraint.")

    return {"Borrado": "Borrada el parte."}
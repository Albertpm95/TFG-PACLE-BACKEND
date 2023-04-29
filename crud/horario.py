from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.horario import Horario


def crear_horario(db: Session, horario_nuevo: str) -> Horario:
    existe_horario: Horario | None = get_horario_nombre(db, horario_nuevo)
    if existe_horario:
        raise HTTPException(
            status_code=404, detail="Ya existe ese horario, no puede crearse otra vez."
        )
    db_horario = Horario(horario=horario_nuevo)
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario


def get_horarios(db: Session) -> list[Horario]:
    return db.query(Horario).all()


def get_horario_id(db: Session, idHorario) -> Horario | None:
    return db.query(Horario).filter(Horario.idHorario == idHorario).first()


def get_horario_nombre(db: Session, horario: str) -> Horario | None:
    return db.query(Horario).filter(Horario.horario == horario).first()


def delete_horario_id(db: Session, idHorario: int) -> dict[str, str]:
    existe_lenguaje: Horario | None = get_horario_id(db, idHorario)
    if not existe_lenguaje:
        raise HTTPException(
            status_code=404, detail="No existe ese horario, no puede borrarse."
        )
    db.delete(existe_lenguaje)
    
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Cannot delete row due to foreign key constraint.")

    return {"Borrado": "Borrado el idioma ${lenguaje.lenguaje}"}
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.horario import Horario as mod_horarios


def crear_horario(db: Session, horario_nuevo: str):
    existe_horario = get_horario_nombre(db, horario_nuevo)
    if existe_horario:
        raise HTTPException(
            status_code=404, detail="Ya existe ese horario, no puede crearse otra vez."
        )
    if not existe_horario:
        db_horario = mod_horarios(horario=horario_nuevo)
        db.add(db_horario)
        db.commit()
        db.refresh(db_horario)
        return db_horario


def get_horarios(db: Session):
    return db.query(mod_horarios.Horarios).all()


def get_horario_id(db: Session, id_horario):
    return db.query(mod_horarios.Horarios).filter_by(id_horario=id_horario).first()


def get_horario_nombre(db: Session, horario: str):
    return db.query(mod_horarios.Horarios).filter_by(horario=horario).first()

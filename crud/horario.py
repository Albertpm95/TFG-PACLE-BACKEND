from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.horario import Horario

def crear_horario(db: Session, horario_nuevo: str):

    existe_horario = get_horario_nombre(db, horario_nuevo)
    if existe_horario:
        raise HTTPException(
            status_code=404, detail="Ya existe ese horario, no puede crearse otra vez."
        )
    if not existe_horario:
        db_horario = Horario(horario=horario_nuevo)
        db.add(db_horario)
        db.commit()
        db.refresh(db_horario)
        return db_horario


def get_horarios(db: Session):
    return db.query(Horario).all()


def get_horario_id(db: Session, idHorario):
    return db.query(Horario).filter_by(idHorario=idHorario).first()


def get_horario_nombre(db: Session, horario: str):
    return db.query(Horario).filter_by(horario=horario).first()

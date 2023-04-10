from fastapi import HTTPException
from sqlalchemy.orm import Session
from crud import fakeDB

from models.horario import Horario as mod_horario

def crear_horario(db: Session, horario_nuevo: str):
  return fakeDB.horario1
  existe_horario = get_horario_nombre(db, horario_nuevo)
  if existe_horario:
    raise HTTPException(
        status_code=404, detail="Ya existe ese horario, no puede crearse otra vez."
    )
  if not existe_horario:
    db_horario = mod_horario(horario=horario_nuevo)
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario


def get_horarios(db: Session):
  return fakeDB.listHorario
  return db.query(mod_horario).all()


def get_horario_id(db: Session, idHorario):
  return fakeDB.horario1
  return db.query(mod_horario).filter_by(idHorario=idHorario).first()


def get_horario_nombre(db: Session, horario: str):
    
  return fakeDB.horario1
  return db.query(mod_horario).filter_by(horario=horario).first()

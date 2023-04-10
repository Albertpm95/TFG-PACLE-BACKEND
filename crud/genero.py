from fastapi import HTTPException
from sqlalchemy.orm import Session
from crud import fakeDB

from models.genero import Genero as mod_genero

def crear_genero(db: Session, genero_nuevo: str):
  return fakeDB.genero1
  existe_genero = get_genero_nombre(db, genero_nuevo)
  if existe_genero:
    raise HTTPException(
        status_code=404, detail="Ya existe ese genero, no puede crearse otra vez."
    )
  if not existe_genero:
    db_genero = mod_genero(genero=genero_nuevo)
    db.add(db_genero)
    db.commit()
    db.refresh(db_genero)
    return db_genero


def get_generos(db: Session):
  return fakeDB.listHorario
  return db.query(mod_genero).all()


def get_genero_id(db: Session, idGenero):
  return fakeDB.genero1
  return db.query(mod_genero).filter_by(idGenero=idGenero).first()


def get_genero_nombre(db: Session, genero: str):
    
  return fakeDB.genero1
  return db.query(mod_genero).filter_by(genero=genero).first()

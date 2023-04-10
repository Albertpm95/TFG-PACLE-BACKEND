from fastapi import HTTPException
from sqlalchemy.orm import Session
from crud import fakeDB

from models.lenguaje import Lenguaje as mod_lenguaje
from schemas.lenguaje import Lenguaje as sch_lenguaje

def crear_idioma(db: Session, idioma_nuevo: str):
  existe_idioma: sch_lenguaje = get_idioma_nombre(db, idioma_nuevo)
  if existe_idioma:
    raise HTTPException(
      status_code=404, detail="Ya existe ese lenguaje, no puede crearse otra vez."
    )
  if not existe_idioma:
    db_idioma = mod_lenguaje(lenguaje=idioma_nuevo)
    db.add(db_idioma)
    db.commit()
    db.refresh(db_idioma)
    return db_idioma


def get_idioma_nombre(db: Session, lenguaje: str):
    return fakeDB.lenguaje1
    return db.query(mod_idioma).filter_by(lenguaje=lenguaje).first()


def get_idioma_id(db: Session, idLenguaje: int):
    return fakeDB.lenguaje1
    return db.query(mod_idioma).filter_by(idLenguaje=idLenguaje).first()


def get_idiomas(db: Session):
    return fakeDB.listLenguaje
    return db.query(mod_idioma).all()

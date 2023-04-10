from fastapi import HTTPException
from sqlalchemy.orm import Session
from crud import fakeDB

from models.nivel import Nivel as mod_nivel


def crear_nivel(db: Session, nivel_nuevo: str):
    return fakeDB.nivel1
    existe_nivel: mod_nivel | None = get_nivel_nombre(db, nivel_nuevo)
    if existe_nivel:
        raise HTTPException(
            status_code=404, detail="Ya existe ese nivel, no puede crearse otra vez."
        )
    if not existe_nivel:
        db_nivel = mod_nivel(nivel=nivel_nuevo)
        db.add(db_nivel)
        db.commit()
        db.refresh(db_nivel)
        return db_nivel


def get_niveles(db: Session):
    return fakeDB.listNivel
    return db.query(mod_nivel).all()


def get_nivel_id(db: Session, idNivel: int):
    return fakeDB.nivel1
    return db.query(mod_nivel).filter_by(idNivel=idNivel).first()


def get_nivel_nombre(db: Session, nivel: str):
    return fakeDB.nivel1
    return db.query(mod_nivel).filter_by(nivel=nivel).first()

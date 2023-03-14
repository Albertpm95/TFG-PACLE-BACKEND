from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.nivel import Nivel as mod_nivel


def crear_nivel(db: Session, nivel_nuevo: str):
    existe_nivel = get_nivel_nombre(db, nivel_nuevo)
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
    return db.query(mod_nivel).all()


def get_nivel_id(db: Session, id_nivel):
    return db.query(mod_nivel).filter_by(id_nivel=id_nivel).first()


def get_nivel_nombre(db: Session, nivel: str):
    return db.query(mod_nivel).filter_by(nivel=nivel).first()

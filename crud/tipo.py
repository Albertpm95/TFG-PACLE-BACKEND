from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.tipos import Tipos as mod_tipos


def crear_idioma(db: Session, tipo_nuevo: str):
    existe_tipo = get_tipo_nombre(db, tipo_nuevo)
    if existe_tipo:
        raise HTTPException(
            status_code=404, detail="Ya existe ese tipo, no puede crearse otra vez."
        )
    if not existe_tipo:
        db_tipo = mod_tipos(idioma=tipo_nuevo)
        db.add(db_tipo)
        db.commit()
        db.refresh(db_tipo)
        return db_tipo


def get_tipos(db: Session):
    return db.query(mod_tipos).all()


def get_tipo_id(db: Session, id_tipo):
    return db.query(mod_tipos).filter_by(id_tipo=id_tipo).first()


def get_tipo_nombre(db: Session, tipo):
    return db.query(mod_tipos).filter_by(tipo=tipo).first()

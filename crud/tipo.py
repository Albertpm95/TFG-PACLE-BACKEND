from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.tipo import Tipo as mod_tipos


def crear_tipo(db: Session, tipo_nuevo: str):
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
    tipos = db.query(mod_tipos).all()
    if not tipos:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido recuperar la tipos de tipos o esta vacia.",
        )
    return tipos


def get_tipo_id(db: Session, id_tipo):
    return db.query(mod_tipos).filter_by(id_tipo=id_tipo).first()


def get_tipo_nombre(db: Session, tipo):
    return db.query(mod_tipos).filter_by(tipo=tipo).first()

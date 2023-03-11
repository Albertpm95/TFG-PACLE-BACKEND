from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.lenguaje import Lenguaje as mod_idioma


def crear_idioma(db: Session, idioma_nuevo: str):
    existe_idioma = get_idioma_nombre(db, idioma_nuevo)
    if existe_idioma:
        raise HTTPException(
            status_code=404, detail="Ya existe ese lenguaje, no puede crearse otra vez."
        )
    if not existe_idioma:
        db_idioma = mod_idioma(lenguaje=idioma_nuevo)
        db.add(db_idioma)
        db.commit()
        db.refresh(db_idioma)
        return db_idioma


def get_idioma_nombre(db: Session, lenguaje: str):
    return db.query(mod_idioma).filter_by(lenguaje=lenguaje).first()


def get_idioma_id(db: Session, id_lenguaje: int):
    return db.query(mod_idioma).filter_by(lenguaje=id_lenguaje).first()


def get_idiomas(db: Session):
    return db.query(mod_idioma).all()

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.idiomas import Idiomas as mod_idioma


def crear_idioma(db: Session, idioma_nuevo: str):
    existe_idioma = get_idioma_nombre(db, idioma_nuevo)
    if existe_idioma:
        raise HTTPException(
            status_code=404, detail="Ya existe ese idioma, no puede crearse otra vez."
        )
    if not existe_idioma:
        db_idioma = mod_idioma(idioma=idioma_nuevo)
        db.add(db_idioma)
        db.commit()
        db.refresh(db_idioma)
        return db_idioma


def get_idioma_nombre(db: Session, idioma: str):
    return db.query(mod_idioma).filter_by(idioma=idioma).first()


def get_idioma_id(db: Session, idioma: str):
    return db.query(mod_idioma).filter_by(idioma=idioma).first()


def get_idiomas(db: Session):
    return db.query(mod_idioma).all()

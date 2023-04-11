from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.lenguaje import Lenguaje



def crear_lenguaje(db: Session, lenguaje_nuevo: str) -> Lenguaje:
    existe_lenguaje: Lenguaje | None = get_idioma_nombre(db, lenguaje_nuevo)
    if existe_lenguaje:
        raise HTTPException(
            status_code=404, detail="Ya existe ese lenguaje, no puede crearse otra vez."
        )
    db_lenguaje = Lenguaje(lenguaje=lenguaje_nuevo)
    db.add(db_lenguaje)
    db.commit()
    db.refresh(db_lenguaje)
    return db_lenguaje


def get_idioma_nombre(db: Session, lenguaje: str):
    return db.query(Lenguaje).filter_by(lenguaje=lenguaje).first()


def get_idioma_id(db: Session, idLenguaje: int):
    return db.query(Lenguaje).filter_by(idLenguaje=idLenguaje).first()


def get_idiomas(db: Session):
    return db.query(Lenguaje).all()
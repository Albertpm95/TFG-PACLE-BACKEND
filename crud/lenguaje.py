from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.lenguaje import Lenguaje


def get_idiomas(db: Session) -> list[Lenguaje]:
    return db.query(Lenguaje).all()


def crear_lenguaje(db: Session, lenguaje_nuevo: str) -> Lenguaje:
    existe_lenguaje: Lenguaje | None = get_idioma_nombre(db, lenguaje_nuevo)
    if existe_lenguaje:
        raise HTTPException(
            status_code=409, detail="Ya existe ese lenguaje, no puede crearse otra vez."
        )
    db_lenguaje = Lenguaje(lenguaje=lenguaje_nuevo)
    db.add(db_lenguaje)
    db.commit()
    db.refresh(db_lenguaje)
    return db_lenguaje


def get_idioma_nombre(db: Session, lenguaje: str) -> Lenguaje | None:
    return db.query(Lenguaje).filter(Lenguaje.lenguaje == lenguaje).first()


def get_idioma_id(db: Session, idLenguaje: int) -> Lenguaje | None:
    return db.query(Lenguaje).filter(Lenguaje.idLenguaje == idLenguaje).first()


def delete_idioma_id(db: Session, idLenguaje: int) -> dict[str, str]:
    existe_lenguaje: Lenguaje | None = get_idioma_id(db, idLenguaje)
    if not existe_lenguaje:
        raise HTTPException(
            status_code=404, detail="No existe ese lenguaje, no puede borrarse."
        )
    db.delete(existe_lenguaje)
    
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Cannot delete row due to foreign key constraint.")

    return {"Borrado": "Borrado el idioma ${lenguaje.lenguaje}"}
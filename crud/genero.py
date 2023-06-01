from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.genero import Genero

def crear_genero(db: Session, genero_nuevo: str) -> Genero:
    existe_genero: Genero = get_genero_nombre(db, genero_nuevo)
    if existe_genero:
        raise HTTPException(
            status_code=409, detail="Ya existe ese genero, no puede crearse otra vez."
        )
    db_genero = Genero(genero=genero_nuevo)
    db.add(db_genero)
    db.commit()
    db.refresh(db_genero)
    return db_genero


def get_generos(db: Session) -> list[Genero]:
    return db.query(Genero).all()


def get_genero_id(db: Session, idGenero) -> Genero:
    return db.query(Genero).filter(Genero.idGenero == idGenero).first()


def get_genero_nombre(db: Session, genero: str) -> Genero:
    return db.query(Genero).filter(Genero.genero == genero).first()


def delete_genero_id(db: Session, idGenero: int) -> dict[str, str]:
    existe_genero: Genero = get_genero_id(db, idGenero)
    if not existe_genero:
        raise HTTPException(
            status_code=404, detail="No existe ese genero, no puede borrarse."
        )
    db.delete(existe_genero)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Cannot delete row due to foreign key constraint.")

    return {"Borrado": "Borrado el idioma ${lenguaje.lenguaje}"}
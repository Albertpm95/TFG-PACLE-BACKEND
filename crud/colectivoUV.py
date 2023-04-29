from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.colectivoUV import ColectivoUV


def crear_colectivoUV(db: Session, colectivoUV_nuevo: str) -> ColectivoUV:
    existe_colectivoUV: ColectivoUV = get_colectivoUV_nombre(db, colectivoUV_nuevo)
    if existe_colectivoUV:
        raise HTTPException(
            status_code=404,
            detail="Ya existe ese colectivoUV, no puede crearse otra vez.",
        )
    db_colectivoUV = ColectivoUV(colectivoUV=colectivoUV_nuevo)
    db.add(db_colectivoUV)
    db.commit()
    db.refresh(db_colectivoUV)
    return db_colectivoUV


def get_colectivosUV(db: Session) -> list[ColectivoUV]:
    return db.query(ColectivoUV).all()


def get_colectivoUV_id(db: Session, idColectivoUV) -> ColectivoUV:
    return (
        db.query(ColectivoUV).filter(ColectivoUV.idColectivoUV == idColectivoUV).first()
    )


def get_colectivoUV_nombre(db: Session, colectivoUV: str) -> ColectivoUV:
    return db.query(ColectivoUV).filter(ColectivoUV.colectivoUV == colectivoUV).first()


def delete_colectivoUV_id(db: Session, idcolectivoUV: int) -> dict[str, str]:
    existe_colectivoUV: ColectivoUV = get_colectivoUV_id(db, idcolectivoUV)
    if not existe_colectivoUV:
        raise HTTPException(
            status_code=404, detail="No existe ese colectivoUV, no puede borrarse."
        )
    db.delete(existe_colectivoUV)
    
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Cannot delete row due to foreign key constraint.")

    return {"Borrado": "Borrado el idioma ${lenguaje.lenguaje}"}

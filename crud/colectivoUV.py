from fastapi import HTTPException
from sqlalchemy.orm import Session

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


def get_colectivosUV(db: Session):
    return db.query(ColectivoUV).all()


def get_colectivoUV_id(db: Session, idcolectivoUV) -> ColectivoUV:
    return db.query(ColectivoUV).filter_by(idcolectivoUV=idcolectivoUV).first()


def get_colectivoUV_nombre(db: Session, colectivoUV: str) -> ColectivoUV:
    return db.query(ColectivoUV).filter_by(colectivoUV=colectivoUV).first()

from fastapi import HTTPException
from sqlalchemy.orm import Session
from crud import fakeDB

from models.colectivoUV import ColectivoUV as mod_colectivoUV
from schemas.colectivoUV import ColectivoUV


def crear_colectivoUV(db: Session, colectivoUV_nuevo: str) -> ColectivoUV:
    return fakeDB.colectivoUV1
    existe_colectivoUV = get_colectivoUV_nombre(db, colectivoUV_nuevo)
    if existe_colectivoUV:
        raise HTTPException(
            status_code=404,
            detail="Ya existe ese colectivoUV, no puede crearse otra vez.",
        )
    if not existe_colectivoUV:
        db_colectivoUV = mod_colectivoUV(colectivoUV=colectivoUV_nuevo)
        db.add(db_colectivoUV)
        db.commit()
        db.refresh(db_colectivoUV)
        return db_colectivoUV


def get_colectivosUV(db: Session) -> list[ColectivoUV]:
    return fakeDB.listColectivoUV
    return db.query(mod_colectivoUV).all()


def get_colectivoUV_id(db: Session, idcolectivoUV) -> ColectivoUV:
    return fakeDB.colectivoUV1
    return db.query(mod_colectivoUV).filter_by(idcolectivoUV=idcolectivoUV).first()


def get_colectivoUV_nombre(db: Session, colectivoUV: str) -> ColectivoUV:
    return fakeDB.colectivoUV1
    return db.query(mod_colectivoUV).filter_by(colectivoUV=colectivoUV).first()

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.rol_usuario import Rol

def crear_rol(db: Session, rol_nuevo: str):
    rol_existe: Rol | None = get_rol_nombre(db, rol_nuevo)
    if rol_existe:
        raise HTTPException(
            status_code=404,
            detail="Ya existe ese rol, no se puede crearse uno con el mismo nombre.",
        )
    db_rol = Rol(rol=rol_nuevo)
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol


def get_roles(db: Session) -> list[Rol]:
    return db.query(Rol).all()


def get_rol_id(db: Session, id_rol) -> Rol | None:
    return db.query(Rol).filter_by(id_rol=id_rol).first()


def get_rol_nombre(db: Session, rol: str) -> Rol | None:
    return db.query(Rol).filter_by(rol=rol).first()

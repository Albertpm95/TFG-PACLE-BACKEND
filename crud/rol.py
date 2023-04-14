from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.rol_usuario import Rol


def crear_rol(db: Session, rol_nuevo: str):
    rol_existe: Rol = get_rol_nombre(db, rol_nuevo)
    if rol_existe:
        raise HTTPException(
            status_code=404,
            detail="Ya existe ese rol, no se puede crearse uno con el mismo nombre.",
        )
    db_rol = Rol(rol=rol_nuevo)
    print(rol_existe)
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol


def get_roles(db: Session) -> list[Rol]:
    return db.query(Rol).all()


def get_rol_id(db: Session, idRol) -> Rol:
    return db.query(Rol).filter(Rol.idRol == idRol).first()


def get_rol_nombre(db: Session, rol: str) -> Rol:
    return db.query(Rol).filter(Rol.rol == rol).first()

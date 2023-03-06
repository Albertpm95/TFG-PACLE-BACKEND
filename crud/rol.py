from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.rol_usuario import Rol as mod_rol


def crear_rol(db: Session, rol_nuevo: str):
    rol_existe = get_rol_nombre(db, rol_nuevo)
    if rol_existe:
        raise HTTPException(
            status_code=404,
            detail="Ya existe ese rol, no se puede crearse uno con el mismo nombre.",
        )
    if not rol_existe:
        db_rol = mod_rol(rol=rol_nuevo)
        db.add(db_rol)
        db.commit()
        db.refresh(db_rol)
        return db_rol


def get_roles(db: Session):
    return db.query(mod_rol).all()


def get_rol_id(db: Session, id_rol):
    return db.query(mod_rol).filter_by(id_rol=id_rol).first()


def get_rol_nombre(db: Session, rol: str):
    return db.query(mod_rol).filter_by(rol=rol).first()

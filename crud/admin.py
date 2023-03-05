from fastapi import HTTPException
from sqlalchemy.orm import Session

from crud import crud
from crud.usuario import get_rol_nombre
from models.usuario import Usuario as mod_usuario
from models.rol_usuario import Rol as mod_rol


def crear_rol(db: Session, rol: str):
    rol = get_rol_nombre(db, rol)
    if rol:
        raise HTTPException(
            status_code=404,
            detail="Ya existe ese rol, no se puede crearse uno con el mismo nombre.",
        )
    if not rol:
        db_rol = mod_rol(rol=rol)
        db.add(db_rol)
        db.commit()
        db.refresh(db_rol)
        return db_rol

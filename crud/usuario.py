from fastapi import HTTPException
from sqlalchemy.orm import Session

from crud import crud
from models.usuario import Usuario as mod_usuario
from schemas.usuario import (
    UsuarioLogin as sch_UsuarioLogin,
    UsuarioOptional as sch_UsuarioOptional,
)
from schemas.usuario import UsuarioBase as sch_UsuarioBase

""" CRUD Principal """


def get_user_username(db: Session, username: str):
    return db.query(mod_usuario).filter(mod_usuario.username == username).first()


""" Deberian requerir permisos de administrador """  # TODO Revisar


def get_user_id(db: Session, id_usuario: str):
    return db.query(mod_usuario).filter(mod_usuario.id_usuario == id_usuario).first()


def get_users(db: Session):
    return db.query(mod_usuario).all()


def alta_usuario(db: Session, usuario: sch_UsuarioLogin):
    db_usuario = mod_usuario(
        username=usuario.username,
        estado=True,
        hashed_password=crud.fake_hash_password(usuario.hashed_password),
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        rol=usuario.rol,
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def update_usuario(db: Session, id_usuario: str, usuario_updated: sch_UsuarioOptional):
    db_usuario = get_user_id(db, id_usuario)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    model_usuario = sch_UsuarioBase(**db_usuario)
    update_usuario_data = usuario_updated.dict(exclude_unset=True)
    db_usuario_updated = model_usuario.copy(update=update_usuario_data)
    db.add(db_usuario_updated)
    db.commit()
    db.refresh(db_usuario_updated)
    return db_usuario_updated


def desactivar_usuario(db: Session, id_usuario: str):
    db_usuario = get_user_id(db, id_usuario)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    setattr(db_usuario, "estado", False)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def activar_usuario(db: Session, id_usuario: str):
    db_usuario = get_user_id(db, id_usuario)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    setattr(db_usuario, "estado", True)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

from fastapi import HTTPException
from sqlalchemy import update
from sqlalchemy.orm import Session

from crud import crud
from models.usuario import Usuario as mod_usuario
from schemas.usuario import UsuarioLogin as sch_UsuarioLogin
from schemas.usuario import UsuarioBase as sch_UsiarioBase

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


def update_usuario(db: Session, usuario_updated: sch_UsiarioBase):
    db_usuario = get_user_id(db, str(usuario_updated.id_usuario))
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in db_usuario.__dict__:
        setattr(db_usuario, key, value)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

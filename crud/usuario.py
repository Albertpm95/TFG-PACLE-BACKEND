from operator import mod
from fastapi import HTTPException
from sqlalchemy.orm import Session

from crud import crud, fakeDB
from crud.rol import get_rol_id
from models.usuario import Usuario as mod_usuario
from schemas.usuario import (
    UsuarioCreacion as sch_UsuarioCreacion,
    UsuarioDB,
    UsuarioLogin,
    UsuarioOptional as sch_UsuarioOptional,
)
from schemas.usuario import UsuarioBase as sch_UsuarioBase

""" CRUD Principal """


def get_user_username(db: Session, username: str) -> UsuarioDB:
    return fakeDB.usuario1
    return db.query(mod_usuario).filter(mod_usuario.username == username).first()


def get_user_login(db: Session, username: str) -> UsuarioLogin:
    return fakeDB.usuarioLogin
    return db.query(mod_usuario).filter(mod_usuario.username == username).first()


""" Deberian requerir permisos de administrador """


def get_user_id(db: Session, id_usuario: str) -> UsuarioDB:
    return fakeDB.usuario1
    return db.query(mod_usuario).filter(mod_usuario.id_usuario == id_usuario).first()


def get_users(db: Session) -> list[UsuarioDB]:
    return fakeDB.listUsuario
    return db.query(mod_usuario).all()


def create_usuario(db: Session, usuario: sch_UsuarioCreacion) -> UsuarioDB:
    existe_usuario = get_user_username(db, username=usuario.username)
    if existe_usuario:
        raise HTTPException(
            status_code=404, detail="Ya existe un usuario con ese username."
        )
    rol = get_rol_id(db, usuario.rol.id_rol)
    if not rol:
        raise HTTPException(status_code=404, detail="No existe el rol")
    db_usuario = mod_usuario(
        username=usuario.username,
        estado=True,
        hashed_password=crud.get_password_hash(usuario.plain_password),
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        id_rol=rol.id_rol,
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def update_usuario(
    db: Session, id_usuario: str, usuario_updated: sch_UsuarioOptional
) -> UsuarioDB:
    return fakeDB.usuario1
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


def desactivar_usuario(db: Session, id_usuario: str) -> UsuarioDB:
    db_usuario: UsuarioDB = get_user_id(db, id_usuario)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    setattr(db_usuario, "estado", False)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def activar_usuario(db: Session, id_usuario: str) -> UsuarioDB:
    db_usuario: UsuarioDB = get_user_id(db, id_usuario)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    setattr(db_usuario, "estado", True)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


""" CRUD APOYO """

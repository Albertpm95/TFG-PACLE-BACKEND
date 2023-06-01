from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from crud import crud
from crud.rol import get_rol_id
from models.rol_usuario import Rol
from models.usuario import Usuario
from schemas.usuario import UsuarioBase, UsuarioDB

""" CRUD Principal """


def get_user_username(db: Session, username: str) -> Usuario:
    return db.query(Usuario).filter(Usuario.username == username).first()


""" Deberian requerir permisos de administrador """


def get_users(db: Session) -> list[Usuario]:
    return db.query(Usuario).all()


def create_usuario(db: Session, usuario_nuevo: UsuarioBase) -> Usuario:
    existe_usuario: Usuario = get_user_username(db, username=usuario_nuevo.username)
    if existe_usuario:
        raise HTTPException(
            status_code=409, detail="Ya existe un usuario con ese username."
        )
    existe_rol: Rol = get_rol_id(db, usuario_nuevo.rol.idRol)
    if not existe_rol:
        raise HTTPException(status_code=404, detail="No existe el rol")
    db_usuario = Usuario(
        username=usuario_nuevo.username,
        estado=True,
        nombre=usuario_nuevo.nombre,
        apellidos=usuario_nuevo.apellidos,
        rol=existe_rol,
        hashedPassword=crud.get_password_hash('1234')
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def get_user_id(db: Session, idUsuario: int) -> Usuario:
    return db.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()


def update_usuario(db: Session, usuario_editado: UsuarioDB):
    existe_usuario = get_user_id(db, usuario_editado.idUsuario)
    existe_rol = get_rol_id(db, existe_usuario.rol.idRol)

    if not existe_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    if not existe_rol:
        raise HTTPException(status_code=404, detail="El rol no existe.")

    existe_usuario.idUsuario = usuario_editado.idUsuario  # type: ignore
    existe_usuario.username = usuario_editado.username  # type: ignore
    existe_usuario.estado = usuario_editado.estado  # type: ignore
    existe_usuario.nombre = usuario_editado.nombre  # type: ignore
    existe_usuario.apellidos = usuario_editado.apellidos  # type: ignore
    existe_usuario.rol = existe_rol

    # TODO Not updating. Issues with nested objects.
    db.commit()
    db.refresh(existe_usuario)
    return existe_usuario


def desactivar_usuario(db: Session, idUsuario: int) -> Usuario:
    db_usuario: Usuario = get_user_id(db, idUsuario)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    setattr(db_usuario, "estado", False)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def activar_usuario(db: Session, idUsuario: int) -> Usuario:
    db_usuario: Usuario = get_user_id(db, idUsuario)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    setattr(db_usuario, "estado", True)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_user(db: Session, idUsuario: int):
    existe_acta: Usuario = get_user_id(db, idUsuario)
    if not existe_acta:
        raise HTTPException(
            status_code=404, detail="No existe ese usuario, no puede borrarse."
        )
    db.delete(existe_acta)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        desactivar_usuario(db, idUsuario)
        raise HTTPException(status_code=400, detail="No se ha podido borrar el usuario para mantener la integridad de la BBDD. Se ha desactivado.")

    return {"Borrado": "Borrado el usuario."}
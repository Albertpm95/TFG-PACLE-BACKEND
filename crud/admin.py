from sqlalchemy.orm import Session

from crud import crud
from models.usuario import Usuario as mod_usuario
from schemas.usuario import UsuarioLogin as sch_UsuarioLogin


def get_user_id(db: Session, id_usuario: str):
    return db.query(mod_usuario).filter(mod_usuario.id_usuario == id_usuario).first()


def get_user_username(db: Session, username: str):
    return db.query(mod_usuario).filter(mod_usuario.username == username).first()


def get_users(db: Session):
    return db.query(mod_usuario).all()


def alta_usuario(db: Session, usuario: sch_UsuarioLogin):
    db_usuario = mod_usuario(
        username=usuario.username,
        active=True,
        hashed_password=crud.fake_hash_password(usuario.hashed_password),
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        rol=usuario.rol,
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

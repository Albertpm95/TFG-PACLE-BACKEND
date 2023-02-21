from fastapi import Query
from sqlalchemy.orm import Session

from db.database import SessionLocal

import models.idiomas
import models.tipos
import models.horarios
import models.usuario
import schemas

from schemas.usuario import UsuarioLogin


def fake_hash_password(password: str):  # TODO Delete
    return "fakehashed" + password


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_id(db: Session, id_usuario: str):
    return (
        db.query(models.usuario.Usuarios)
        .filter(models.usuario.Usuarios.id_usuario == id_usuario)
        .first()
    )


def get_user_username(db: Session, username: str):
    return (
        db.query(models.usuario.Usuarios)
        .filter(models.usuario.Usuarios.username == username)
        .first()
    )


def get_users(db: Session):
    return db.query(models.usuario.Usuarios).all()


def alta_usuario(db: Session, usuario: UsuarioLogin):
    db_usuario = models.usuario.Usuarios(
        username=usuario.username,
        active=True,
        hashed_password=fake_hash_password(usuario.hashed_password),
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        rol=usuario.rol,
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario



def create_alumno(db: Session, alumno: alumno_sch.AlumnoActa):
    alumno_db = alumno_mod.Alumno(**alumno.dict())
    db.add(alumno_db)
    db.commit()
    db.refresh(alumno_db)
    return alumno_db


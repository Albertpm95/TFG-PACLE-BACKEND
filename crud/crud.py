from sqlalchemy.orm import Session

from db.database import SessionLocal

import models.idiomas
import schemas


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_idiomas(db: Session):
    return db.query(models.idiomas.Idiomas).all()


def add_idiomas(db: Session, lenguaje: str):
    db_idioma = models.idiomas.Idiomas(lenguaje=lenguaje)
    db.add(db_idioma)
    db.commit()
    db.refresh(db_idioma)
    return db_idioma


""" 

def get_user_id(db: Session, id_usuario: str):
    return (
        db.query(usuario_mod.Usuarios)
        .filter(usuario_mod.Usuarios.id_usuario == id_usuario)
        .first()
    )


def get_user_username(db: Session, username: str):
    return (
        db.query(usuario_mod.Usuarios)
        .filter(usuario_mod.Usuarios.username == username)
        .first()
    )


def get_users(db: Session):
    return db.query(usuario_mod.Usuarios).all()


def create_user(db: Session, usuario: usuario_sch.UsuarioFront):
    fake_hashed_password = usuario.username + "notreallyhashed"
    db_user = usuario_mod.Usuarios(
        username=usuario.username,
        hashed_password=fake_hashed_password,
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        active=True,
        rol=usuario.rol,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_alumno(db: Session, alumno: alumno_sch.AlumnoActa):
    alumno_db = alumno_mod.Alumno(**alumno.dict())
    db.add(alumno_db)
    db.commit()
    db.refresh(alumno_db)
    return alumno_db
"""

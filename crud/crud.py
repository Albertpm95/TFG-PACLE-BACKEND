from fastapi import Query
from pydantic import validate_arguments
from sqlalchemy.orm import Session

from db.database import SessionLocal

import models.idiomas
import models.tipos
import models.horarios
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


def add_idioma(db: Session, lenguaje: str):
    db_idioma = models.idiomas.Idiomas(lenguaje=lenguaje)
    db.add(db_idioma)
    db.commit()
    db.refresh(db_idioma)
    return db_idioma


def get_tipos(db: Session):
    return db.query(models.tipos.Tipos).all()


def add_tipo(db: Session, tipo: str):
    db_tipo = models.tipos.Tipos(tipo=tipo)
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo


def get_horarios(db: Session):
    return db.query(models.horarios.Horarios).all()


def add_horario(
    db: Session,
    horario: str = Query(regex="/^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/"),
):
    db_horario = models.horarios.Horarios(horario=horario)
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario


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

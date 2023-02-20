from sqlalchemy.orm import Session

from db.database import Base, SessionLocal, engine
from models import alumno as alumno_mod
from models import usuario as usuario_mod
from schemas import alumno as alumno_sch
from schemas import usuario as usuario_sch


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_id(db: Session, id_usuario: str):
    return (
        db.query(usuario_mod.Usuario)
        .filter(usuario_mod.Usuario.id_usuario == id_usuario)
        .first()
    )


def get_user_username(db: Session, username: str):
    return (
        db.query(usuario_mod.Usuario)
        .filter(usuario_mod.Usuario.username == username)
        .first()
    )


def get_users(db: Session):
    return db.query(usuario_mod.Usuario).all()


def create_user(db: Session, usuario: usuario_sch.UsuarioBase):
    fake_hashed_password = usuario.password + "notreallyhashed"
    db_user = usuario_mod.Usuario(
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

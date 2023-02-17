from sqlalchemy.orm import Session
from models import usuario as usuario_mod
from schemas import usuario as usuario_sch


def get_user(db: Session, id_usuario: str):
    return (
        db.query(usuario_mod.Usuario)
        .filter(usuario_mod.Usuario.id_usuario == id_usuario)
        .first()
    )


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(usuario_mod.Usuario).offset(skip).limit(limit).all()


def create_user(db: Session, usuario: usuario_sch.Usuario):
    fake_hashed_password = usuario.password + "notreallyhashed"
    db_user = usuario_mod.Usuario(
        username=usuario.username,
        password=fake_hashed_password,
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        active=True,
        rol=usuario.rol,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

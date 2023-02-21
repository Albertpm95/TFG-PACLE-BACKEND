from fastapi import Query
from sqlalchemy.orm import Session

from db.database import SessionLocal

from schemas import alumno as sch_alumno
from models import alumno as mod_alumno


def create_alumno(alumno: sch_alumno.AlumnoActa, db: Session):
    alumno_db = mod_alumno.Alumno(
        nombre=alumno.nombre, apellidos=alumno.apellidos, dni=alumno.dni
    )
    db.add(alumno_db)
    db.commit()
    db.refresh(alumno_db)
    return alumno_db


def get_alumnos(db: Session):
    return db.query(mod_alumno.Alumno).all()


def get_alumno_nombre(nombre: str, db: Session):
    return db.query(mod_alumno.Alumno).filter_by(nombre=nombre)

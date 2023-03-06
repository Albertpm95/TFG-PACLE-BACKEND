from http.client import HTTPException
from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas import alumno as sch_alumno
from models import alumno as mod_alumno


def create_alumno(alumno: sch_alumno.AlumnoActa, db: Session):
    existe_alumno = get_alumno_dni(alumno.dni, db)
    if existe_alumno:
        raise HTTPException(
            status_code=404, detail="Ya existe ese horario, no puede crearse otra vez."
        )
    if not existe_alumno:
        alumno_db = mod_alumno.Alumno(
            nombre=alumno.nombre, apellidos=alumno.apellidos, dni=alumno.dni
        )
        db.add(alumno_db)
        db.commit()
        db.refresh(alumno_db)
        return alumno_db


def get_alumnos(db: Session):
    return db.query(mod_alumno).all()


def get_alumno_dni(dni: str, db: Session):
    return db.query(mod_alumno).filter_by(dni=dni)


def get_alumno_nombre(nombre: str, db: Session):
    return db.query(mod_alumno).filter_by(nombre=nombre)

from fastapi import HTTPException
from sqlalchemy.orm import Session

import schemas.alumno as sch_alumno
import models.alumno as mod_alumno


def create_alumno(alumno: sch_alumno.Alumno, db: Session):
    existe_alumno = get_alumno_dni(alumno.dni, db)
    if existe_alumno:
        raise HTTPException(
            status_code=404, detail="Ya existe ese alumno, no puede crearse otra vez."
        )
    if not existe_alumno:
        alumno_db = mod_alumno.Alumno(
            nombre=alumno.nombre, apellidos=alumno.apellidos, dni=alumno.dni
        )
        db.add(alumno_db)
        db.commit()
        db.refresh(alumno_db)
        return alumno_db


def update_alumno(alumno: sch_alumno.Alumno, db: Session):
    existe_alumno = get_alumno_dni(alumno.dni, db)
    if not existe_alumno:
        raise HTTPException(status_code=404, detail="El alumno no existe.")
    if existe_alumno:
        alumno_db = mod_alumno.Alumno(
            nombre=alumno.nombre, apellidos=alumno.apellidos, dni=alumno.dni
        )
        db.add(alumno_db)
        db.commit()
        db.refresh(alumno_db)
        return alumno_db


def get_alumnos(db: Session):
    return db.query(mod_alumno.Alumno).all()


def get_alumno_dni(dni: str, db: Session):
    return db.query(mod_alumno.Alumno).filter_by(dni=dni)


def get_alumno_nombre(nombre: str, db: Session):
    return db.query(mod_alumno.Alumno).filter_by(nombre=nombre)


def get_alumno_id(id_alumno: int, db: Session):
    return db.query(mod_alumno.Alumno).filter_by(id_alumno=id_alumno)

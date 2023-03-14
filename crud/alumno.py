from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.alumno import Alumno as sch_alumno
from schemas.alumno import AlumnoDB as sch_alumno_DB
from models.alumno import Alumno as mod_alumno


def create_alumno(alumno: sch_alumno, db: Session):
    existe_alumno = get_alumno_dni(alumno.dni, db)
    if existe_alumno:
        raise HTTPException(
            status_code=404, detail="Ya existe ese alumno, no puede crearse otra vez."
        )
    if not existe_alumno:
        alumno_db = mod_alumno(
            nombre=alumno.nombre, apellidos=alumno.apellidos, dni=alumno.dni
        )
        db.add(alumno_db)
        db.commit()
        db.refresh(alumno_db)
        return alumno_db


def update_alumno(alumno: sch_alumno_DB, db: Session):
    existe_alumno = get_alumno_dni(alumno.dni, db)
    if not existe_alumno:
        raise HTTPException(status_code=404, detail="El alumno no existe.")
    if existe_alumno:
        alumno_db = mod_alumno(
            nombre=alumno.nombre, apellidos=alumno.apellidos, dni=alumno.dni
        )
        db.add(alumno_db)
        db.commit()
        db.refresh(alumno_db)
        return alumno_db


def get_alumnos(db: Session):
    return db.query(mod_alumno).all()


def get_alumno_dni(dni: str, db: Session):
    alumno = db.query(mod_alumno).filter(mod_alumno.dni == dni).first()
    if not alumno:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el alumno solicitado.",
        )
    return alumno


def get_alumno_nombre(nombre: str, db: Session):
    alumno = db.query(mod_alumno).filter(mod_alumno.nombre == nombre).first()
    if not alumno:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el alumno solicitado.",
        )
    return alumno


def get_alumno_id(id_alumno: int, db: Session):
    alumno = db.query(mod_alumno).filter(mod_alumno.id_alumno == id_alumno).first()
    if not alumno:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el alumno solicitado.",
        )
    print(str(db.query(mod_alumno).first()))
    return alumno

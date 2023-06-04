
from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from crud import colectivoUV as crud_colectivoUV
from crud import genero as crud_genero
from models.alumno import Alumno
from models.colectivoUV import ColectivoUV
from models.genero import Genero
from schemas.alumno import Alumno as sch_alumno
from schemas.alumno import AlumnoDB as sch_alumnoDB


def get_alumnos(db: Session):
    return db.query(Alumno).all()


def get_alumno_dni(dni: str, db: Session):
    alumno = db.query(Alumno).filter(Alumno.dni == dni).first()
    return alumno


def get_alumno_nombre(nombre: str, db: Session):
    alumno = db.query(Alumno).filter(Alumno.nombre == nombre).first()
    return alumno


def get_alumno_id(idAlumno: int, db: Session):
    alumno = db.query(Alumno).filter(Alumno.idAlumno == idAlumno).first()
    return alumno


def create_alumno(alumno: sch_alumno, db: Session):
    existe_alumno: Alumno = get_alumno_dni(alumno.dni, db)
    if existe_alumno:
        raise HTTPException(status_code=409, detail="Ya existe ese alumno, no puede crearse otra vez.")

    existe_genero: Genero = crud_genero.get_genero_id(db, alumno.genero.idGenero)
    if not existe_genero:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el Genero seleccionado, no puede registrarse al alumno.",
        )

    existe_colectivoUV: ColectivoUV = crud_colectivoUV.get_colectivoUV_id(
        db=db, idColectivoUV=alumno.colectivoUV.idColectivoUV
    )
    if not existe_colectivoUV:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el Colectivo UV seleccionado, no puede registrarse al alumno.",
        )

    fechaNacimientoDate: datetime = alumno.fechaNacimiento

    alumno_db = Alumno(
        nombre=alumno.nombre,
        apellidos=alumno.apellidos,
        dni=alumno.dni,
        colectivoUV=existe_colectivoUV,
        genero=existe_genero,
        email=alumno.email,
        telefono=alumno.telefono,
        fechaNacimiento=fechaNacimientoDate,
        pruebaAdaptada=alumno.pruebaAdaptada,
    )
    db.add(alumno_db)
    db.commit()
    db.refresh(alumno_db)
    return alumno_db


def update_alumno(alumno: sch_alumnoDB, db: Session):
    existe_alumno: Alumno | None = get_alumno_dni(alumno.dni, db)
    if not existe_alumno:
        raise HTTPException(
            status_code=404,
            detail="No existe el alumno, no se pueden actualizar sus detalles.",
        )
    existe_genero: Genero = crud_genero.get_genero_id(db, alumno.genero.idGenero)
    if not existe_genero:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el Genero seleccionado en la DB, no puede actualizarse al alumno.",
        )
    existe_colectivoUV: ColectivoUV = crud_colectivoUV.get_colectivoUV_id(db, alumno.colectivoUV.idColectivoUV)
    if not existe_colectivoUV:
        raise HTTPException(
            status_code=404,
            detail="No existe ese Colectivo UV seleccionado, no puede actualizarse al alumno.",
        )
    existe_alumno.nombre = alumno.nombre  
    existe_alumno.apellidos = alumno.apellidos
    existe_alumno.dni = alumno.dni 
    existe_alumno.colectivoUV = existe_colectivoUV
    existe_alumno.genero = existe_genero 
    existe_alumno.email = alumno.email  
    existe_alumno.telefono = alumno.telefono
    existe_alumno.fechaNacimiento = alumno.fechaNacimiento
    existe_alumno.pruebaAdaptada = alumno.pruebaAdaptada
    existe_alumno.idAlumno = alumno.idAlumno
    db.add(existe_alumno)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="No se ha podido actualizar el alumno.")
    db.refresh(existe_alumno)
    return existe_alumno


def delete_alumno_id(db: Session, idAlumno: int) -> dict[str, str]:
    existe_alumno: Alumno = get_alumno_id(db=db, idAlumno=idAlumno)
    if not existe_alumno:
        raise HTTPException(status_code=404, detail="No existe el alumno, no puede borrarse.")
    db.delete(existe_alumno)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="No se ha podido borrar el alumno porque algo depende de este.")

    return {"Borrado": "Borrado el idioma ${lenguaje.lenguaje}"}

from datetime import date, datetime
from fastapi import HTTPException
from sqlalchemy import Date
from sqlalchemy.orm import Session

from crud import colectivoUV as crud_colectivoUV, genero as crud_genero

from models.alumno import Alumno

# from models.shared import AlumnosConvocatoria
from models.genero import Genero
from models.colectivoUV import ColectivoUV

from schemas.alumno import Alumno as sch_alumno, AlumnoDB as sch_alumnoDB


def get_alumnos(db: Session):
    return db.query(Alumno).all()


def get_alumnos_by_convocatoria(idConvocatoria: int, db: Session):
    return db.query(Alumno).all()  # TODO Fix
    return (
        db.query(AlumnosConvocatoria)
        .filter(AlumnosConvocatoria.idConvocatoria == idConvocatoria)
        .all()
    )


def get_alumno_dni(dni: str, db: Session):
    return db.query(Alumno).filter(Alumno.dni == dni).first()


def get_alumno_nombre(nombre: str, db: Session):
    return db.query(Alumno).filter(Alumno.nombre == nombre).first()


def get_alumno_id(idAlumno: int, db: Session):
    return db.query(Alumno).filter(Alumno.idAlumno == idAlumno).first()


def create_alumno(alumno: sch_alumno, db: Session):
    existe_alumno: Alumno = get_alumno_dni(alumno.dni, db)
    if existe_alumno:
        raise HTTPException(
            status_code=404, detail="Ya existe ese alumno, no puede crearse otra vez."
        )
    existe_genero: Genero = crud_genero.get_genero_id(db, alumno.genero.idGenero)
    if not existe_genero:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el Genero seleccionado en la DB, no puede registrarse al alumno.",
        )
    existe_colectivoUV: ColectivoUV = crud_colectivoUV.get_colectivoUV_id(
        db, alumno.colectivoUV.idColectivoUV
    )
    if not existe_colectivoUV:
        raise HTTPException(
            status_code=404,
            detail="No existe ese Colectivo UV seleccionado, no puede registrarse al alumno.",
        )
    fechaNacimientoDate: date = alumno.fechaNacimiento
    print(alumno.fechaNacimiento, type(alumno.fechaNacimiento))
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
    existe_colectivoUV: ColectivoUV = crud_colectivoUV.get_colectivoUV_id(
        db, alumno.colectivoUV.idColectivoUV
    )
    if not existe_colectivoUV:
        raise HTTPException(
            status_code=404,
            detail="No existe ese Colectivo UV seleccionado, no puede actualizarse al alumno.",
        )
    existe_alumno.nombre = alumno.nombre  # type: ignore
    existe_alumno.apellidos = alumno.apellidos  # type: ignore
    existe_alumno.dni = alumno.dni  # type: ignore
    existe_alumno.colectivoUV = alumno.colectivoUV  # type: ignore
    existe_alumno.genero = alumno.genero  # type: ignore
    existe_alumno.email = alumno.email  # type: ignore
    existe_alumno.telefono = alumno.telefono  # type: ignore
    existe_alumno.fechaNacimiento = alumno.fechaNacimiento  # type: ignore
    existe_alumno.pruebaAdaptada = alumno.pruebaAdaptada  # type: ignore
    existe_alumno.idAlumno = alumno.idAlumno  # type: ignore
    db.add(existe_alumno)
    db.commit()
    db.refresh(existe_alumno)
    return existe_alumno


def delete_alumno_id(db: Session, idAlumno: int) -> dict[str, str]:
    existe_alumno: Alumno = get_alumno_id(db=db, idAlumno=idAlumno)
    if not existe_alumno:
        raise HTTPException(
            status_code=404, detail="No existe el alumno, no puede borrarse."
        )
    db.delete(existe_alumno)
    db.commit()
    # return {"ok": True}
    return {"Borrado": "Borrado el alumno ${alumno.nombre} ${alumno.apellidos}"}

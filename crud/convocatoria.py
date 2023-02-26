from fastapi import Query, HTTPException
from sqlalchemy.orm import Session

from models import idiomas as mod_idiomas
from models import tipos as mod_tipos
from models import horarios as mod_horarios
from models.convocatoria import Convocatoria as mod_convocatoria
from schemas.convocatoria import Convocatoria as sch_convocatoria

""" CRUD PRINCIPAL """


def get_convocatorias(db: Session):
    convocatorias = db.query(mod_convocatoria).all()
    if not convocatorias:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido recuperar la lista de convocatorias o esta vacia.",
        )
    return convocatorias


def get_convocatorias_activas(db: Session):
    return db.query(mod_convocatoria).filter_by(estado=True).all()


def get_convocatoria_id(id_convocatoria: str, db: Session):
    return db.query(mod_convocatoria).filter(
        mod_convocatoria.id_convocatoria == id_convocatoria
    )


def create_convocatoria(convocatoria: sch_convocatoria, db: Session):
    db_convocatoria = mod_convocatoria(
        comprension_auditiva_puntuacion_maxima_parte=convocatoria.comprension_auditiva_puntuacion_maxima_parte,
        comprension_lectora_puntuacion_maxima_parte=convocatoria.comprension_lectora_puntuacion_maxima_parte,
        expresion_escrita_puntuacion_maxima_parte=convocatoria.expresion_escrita_puntuacion_maxima_parte,
        expresion_oral_puntuacion_maxima_parte=convocatoria.expresion_oral_puntuacion_maxima_parte,
        estado=True,
        fecha=convocatoria.fecha,
        lenguaje=convocatoria.lenguaje,
        tipo=convocatoria.tipo,
        horario=convocatoria.horario,
    )
    db.add(db_convocatoria)
    db.commit()
    db.refresh(db_convocatoria)
    return db_convocatoria


""" CRUD APOYO """


def get_idiomas(db: Session):
    return db.query(mod_idiomas.Idiomas).all()


def get_idioma_id(db: Session, id_idioma):
    return db.query(mod_idiomas.Idiomas).filter_by(id_idioma=id_idioma).first()


def get_tipos(db: Session):
    return db.query(mod_tipos.Tipos).all()


def get_tipo_id(db: Session, id_tipo):
    return db.query(mod_tipos.Tipos).filter_by(id_tipo=id_tipo).first()


def get_horarios(db: Session):
    return db.query(mod_horarios.Horarios).all()


def get_horario_id(db: Session, id_horario):
    return db.query(mod_horarios.Horarios).filter_by(id_horario=id_horario).first()


def add_horario(
    db: Session,
    horario: str = Query(regex="/^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/"),
):
    db_horario = mod_horarios.Horarios(horario=horario)
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario


def add_idioma(lenguaje: str, db: Session):
    db_idioma = mod_idiomas.Idiomas(lenguaje=lenguaje)
    db.add(db_idioma)
    db.commit()
    db.refresh(db_idioma)
    return db_idioma


def add_tipo(db: Session, tipo: str):
    db_tipo = mod_tipos.Tipos(tipo=tipo)
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

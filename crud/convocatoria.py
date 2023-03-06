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


def get_tipos(db: Session):
    return db.query(mod_tipos.Tipos).all()


def get_tipo_id(db: Session, id_tipo):
    return db.query(mod_tipos.Tipos).filter_by(id_tipo=id_tipo).first()


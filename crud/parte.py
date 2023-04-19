from sqlalchemy.orm import Session

from models.parte import Parte
from schemas.parte import ParteBase

from crud import tarea as crud_tarea

def create_parte(parte: ParteBase, db: Session):
    parte_db = Parte(
        puntuacionMaxima=parte.puntuacionMaxima,
        tipo=parte.tipo,
        tareas=[]
    )
    print('Before add ',parte_db)
    db.add(parte_db)
    print('After add ', parte_db)
    db.commit()
    db.refresh(parte_db)
    print('Refreshed: ', parte_db)    
    return parte_db
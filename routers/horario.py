from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import crud
from crud import horario as crud_horario
from schemas.horario import Horario, HorarioBase

router = APIRouter(prefix="/horario", tags=["Horario"])


@router.get("/list", response_model=list[Horario])
async def recuperar_lista_horarios(db: Session = Depends(crud.get_db)):
    return crud_horario.get_horarios(db)


@router.post("/create", response_model=Horario)
async def create_horario(
    horario_nuevo: HorarioBase, db: Session = Depends(crud.get_db)
) -> Horario:
    return crud_horario.crear_horario(db, horario_nuevo.horario)


@router.delete("/delete/{idHorario}", response_model=dict[str, str])
async def delete_horario(idHorario: int, db: Session = Depends(crud.get_db)):
    return crud_horario.delete_horario_id(db, idHorario)

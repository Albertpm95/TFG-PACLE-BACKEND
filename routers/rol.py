from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import rol as crud_rol
from schemas.rol_usuario import Rol, RolBase

router = APIRouter(prefix="/rol", tags=['Rol'])

@router.get("/list", response_model=list[Rol])
async def recuperar_lista_roles(db: Session = Depends(crud.get_db)):
    return crud_rol.get_roles(db)

@router.post("/create", response_model=Rol)
async def create_rol(
    rol_nuevo: RolBase, db: Session = Depends(crud.get_db)
) -> Rol:
    return crud_rol.crear_rol(db, rol_nuevo.rol)
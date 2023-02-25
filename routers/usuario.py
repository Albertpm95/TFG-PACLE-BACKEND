from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import usuario as crud_usuario
from crud import login as crud_login
from schemas.usuario import UsuarioBase

router = APIRouter()


@router.get("/usuario/actual/", response_model=UsuarioBase)
async def recuperar_usuario_actual(
    current_user: UsuarioBase = Depends(crud_login.get_current_active_user),
):
    return current_user


@router.get("/usuario/roles")
async def recuperar_roles_disponibles(db: Session = Depends(crud.get_db)):
    return crud_usuario.get_roles(db)

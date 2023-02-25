from fastapi import APIRouter, Depends

from crud import login as crud_login
from schemas.usuario import UsuarioBase

router = APIRouter()


@router.get("/usuario/actual/", response_model=UsuarioBase)
async def recuperar_usuario_actual(
    current_user: UsuarioBase = Depends(crud_login.get_current_active_user),
):
    return current_user

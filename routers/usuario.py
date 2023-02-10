from fastapi import APIRouter
from constants import lista_acciones
router = APIRouter()


@router.get("/usuarios/actions")
async def get_list_de_acciones():
    return lista_acciones

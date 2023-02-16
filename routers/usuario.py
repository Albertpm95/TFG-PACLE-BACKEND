from fastapi import APIRouter
from fake_db import lista_acciones
router = APIRouter()


@router.get("/usuario/actions")
async def get_lista_de_acciones():
    return lista_acciones

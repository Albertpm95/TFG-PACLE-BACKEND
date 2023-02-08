from fastapi import APIRouter
from constants import fake_alumnos_DB
from schemas.alumno import Alumno
router = APIRouter()


@router.post("/alumno")
async def recuperar_alumno(nombre: str, apellido: str | None = None, acta_id: str | None = None):
    filtrado_1 = ''
    filtrado_2 = ''
    filtrado_3 = ''
    filtrado_1 = filter(lambda x: x.nombre == nombre, fake_alumnos_DB)
    if apellido:
        filtrado_2 = filter(lambda x: x.apellidos == apellido, fake_alumnos_DB)

    '''
    if acta_id:
        filtrado_3 = filter(lambda x: x. == acta_id, fake_alumnos_DB)
    '''
    return {"filtrado_1": filtrado_1, "filtrado_2": filtrado_2, "filtrado_3": filtrado_3}

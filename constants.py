from typing import Literal
from schemas.usuario import UsuarioLogin
from schemas.acta import ActaBase
from schemas.alumno import AlumnoBase
from datetime import datetime
import random  # TODO QUitar

TIPOS_ACTA = Literal["Ordinaria", "Extraordinaria"]
IDIOMAS_DISPONIBLES = Literal[
    "Español", "English", "Català", "Français", "Chainese", "Deutsch"
]
HORARIOS = Literal["9:00"]

lista_acciones = [
    {"action_label": "Crear una convocatoria", "url": "acta/create"},
    {"action_label": "Listar acta", "url": "acta/list"},
    {"action_label": "Cargar CSV", "url": "alumno/upload"},
    {"action_label": "Editar alumnos", "url": "alumno/edit"},
    {"action_label": "Listar alumnos", "url": "alumno/list"},
    {"action_label": "Listar convocatorias estados", "url": "alumno/activo"},
]

fake_usuarios_DB = [
    UsuarioLogin(username="rick_sanchez", password="1234"),
    UsuarioLogin(username="morty_smith", password="1234"),
    UsuarioLogin(username="jerry_smith", password="1234"),
]

fake_actas_DB = [
    ActaBase(
        estado=True,
        lenguaje="Español",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="1",
    ),
    ActaBase(
        estado=True,
        lenguaje="English",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="2",
    ),
    ActaBase(
        estado=True,
        lenguaje="Català",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="3",
    ),
    ActaBase(
        estado=True,
        lenguaje="Français",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="4",
    ),
    ActaBase(
        estado=True,
        lenguaje="Chainese",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="5",
    ),
    ActaBase(
        estado=True,
        lenguaje="Deutsch",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="6",
    ),
    ActaBase(
        estado=False,
        lenguaje="Español",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="7",
    ),
    ActaBase(
        estado=False,
        lenguaje="English",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="8",
    ),
    ActaBase(
        estado=False,
        lenguaje="Català",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="9",
    ),
    ActaBase(
        estado=False,
        lenguaje="Français",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="10",
    ),
    ActaBase(
        estado=False,
        lenguaje="Chainese",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="11",
    ),
    ActaBase(
        estado=False,
        lenguaje="Deutsch",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="12",
    ),
    ActaBase(
        estado=True,
        lenguaje="Español",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="13",
    ),
    ActaBase(
        estado=True,
        lenguaje="English",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="14",
    ),
    ActaBase(
        estado=True,
        lenguaje="Català",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="15",
    ),
    ActaBase(
        estado=True,
        lenguaje="Français",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="16",
    ),
    ActaBase(
        estado=True,
        lenguaje="Chainese",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="17",
    ),
    ActaBase(
        estado=True,
        lenguaje="Deutsch",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="18",
    ),
    ActaBase(
        estado=False,
        lenguaje="Español",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="19",
    ),
    ActaBase(
        estado=False,
        lenguaje="English",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="20",
    ),
    ActaBase(
        estado=False,
        lenguaje="Català",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="21",
    ),
    ActaBase(
        estado=False,
        lenguaje="Français",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="22",
    ),
    ActaBase(
        estado=False,
        lenguaje="Chainese",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="23",
    ),
    ActaBase(
        estado=False,
        lenguaje="Deutsch",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="24",
    ),
    ActaBase(
        estado=True,
        lenguaje="Español",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="25",
    ),
    ActaBase(
        estado=True,
        lenguaje="English",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="26",
    ),
    ActaBase(
        estado=True,
        lenguaje="Català",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="27",
    ),
    ActaBase(
        estado=True,
        lenguaje="Français",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="28",
    ),
    ActaBase(
        estado=True,
        lenguaje="Chainese",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="29",
    ),
    ActaBase(
        estado=True,
        lenguaje="Deutsch",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="30",
    ),
    ActaBase(
        estado=False,
        lenguaje="Español",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="31",
    ),
    ActaBase(
        estado=False,
        lenguaje="English",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="32",
    ),
    ActaBase(
        estado=False,
        lenguaje="Català",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="33",
    ),
    ActaBase(
        estado=False,
        lenguaje="Français",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="34",
    ),
    ActaBase(
        estado=False,
        lenguaje="Chainese",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="35",
    ),
    ActaBase(
        estado=False,
        lenguaje="Deutsch",
        fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)),
        tipo="Extraordinaria",
        id="36",
    ),
]

fake_alumnos_DB = [
    AlumnoBase(id="1", nombre="Bob", apellidos="Swanson"),
    AlumnoBase(id="2", nombre="Albert", apellidos="Swanson"),
    AlumnoBase(id="3", nombre="Billy", apellidos="Billington"),
    AlumnoBase(id="4", nombre="Rick", apellidos="Sanchez"),
    AlumnoBase(id="5", nombre="Jaimito", apellidos="Grimes"),
    AlumnoBase(id="6", nombre="Eustaquio", apellidos="Ramirez"),
    AlumnoBase(id="7", nombre="Firulais", apellidos="Gonzalez"),
    AlumnoBase(id="8", nombre="Waldo", apellidos="Emerson"),
]

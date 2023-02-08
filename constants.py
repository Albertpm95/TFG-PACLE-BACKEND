from schemas.usuario import UsuarioLogin
from schemas.acta import ActaBase
from schemas.alumno import AlumnoBase
from datetime import datetime

now = datetime.utcfromtimestamp(1675673005)

lista_acciones = [
    {"action_label": "Crear una convocatoria",
        "url": "acta/create"},  # Form vacio -> Post
    # Get todas las convocatorias
    {"action_label": "Listar acta", "url": "acta/list"},
    # Put fichero CSV para crear algo
    {"action_label": "Cargar CSV", "url": "cargar"},
    # Get todos los alumnos # Entiendo que para los correctores
    {"action_label": "Listar alumnos", "url": "alumnos"},
    {"action_label": "Listar convocatorias activas", "url": "alumnos/activo"}
]
fake_usuarios_DB = [
    UsuarioLogin(username="rick_sanchez", password="1234"),
    UsuarioLogin(username="morty_smith", password="1234"),
    UsuarioLogin(username="jerry_smith", password="1234")
]
fake_actas_DB = [
    ActaBase(activa=True, lenguage='Español',
             fecha=now, tipo='Extraordinaria', id_acta='1'),
    ActaBase(activa=True, lenguage='English',
             fecha=now, tipo='Extraordinaria', id_acta='2'),
    ActaBase(activa=True, lenguage='Català',
             fecha=now, tipo='Extraordinaria', id_acta='3'),
    ActaBase(activa=True, lenguage='Français',
             fecha=now, tipo='Extraordinaria', id_acta='4'),
    ActaBase(activa=True, lenguage='Chainese',
             fecha=now, tipo='Extraordinaria', id_acta='5'),
    ActaBase(activa=True, lenguage='Deutsch',
             fecha=now, tipo='Extraordinaria', id_acta='6'),
    ActaBase(activa=False, lenguage='Español',
             fecha=now, tipo='Extraordinaria', id_acta='7'),
    ActaBase(activa=False, lenguage='English',
             fecha=now, tipo='Extraordinaria', id_acta='8'),
    ActaBase(activa=False, lenguage='Català',
             fecha=now, tipo='Extraordinaria', id_acta='9'),
    ActaBase(activa=False, lenguage='Français',
             fecha=now, tipo='Extraordinaria', id_acta='10'),
    ActaBase(activa=False, lenguage='Chainese',
             fecha=now, tipo='Extraordinaria', id_acta='11'),
    ActaBase(activa=False, lenguage='Deutsch',
             fecha=now, tipo='Extraordinaria', id_acta='12'),
]

fake_alumnos_DB = [
    AlumnoBase(id='1', nombre='Bob', apellidos='Swanson'),
    AlumnoBase(id='2', nombre='Albert', apellidos='Swanson'),
    AlumnoBase(id='3', nombre='Billy', apellidos='Billington'),
    AlumnoBase(id='4', nombre='Rick', apellidos='Sanchez'),
    AlumnoBase(id='5', nombre='Jaimito', apellidos='Grimes'),
    AlumnoBase(id='6', nombre='Eustaquio', apellidos='Ramirez'),
    AlumnoBase(id='7', nombre='Firulais', apellidos='Gonzalez'),
    AlumnoBase(id='8', nombre='Waldo', apellidos='Emerson')
]

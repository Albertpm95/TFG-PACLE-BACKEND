from schemas.usuario import UsuarioLogin
from schemas.acta import ActaBase
from schemas.alumno import AlumnoBase
from datetime import datetime

now = datetime.utcfromtimestamp(1675673005)

lista_acciones = [
    {"action_label": "Crear una convocatoria",
        "url": "actas/create"},  # Form vacio -> Post
    # Get todas las convocatorias
    {"action_label": "Listar acta", "url": "actas/list"},
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
    ActaBase(activa=True, lenguaje='Español',
             fecha=now, tipo='Extraordinaria', id_acta='1'),
    ActaBase(activa=True, lenguaje='English',
             fecha=now, tipo='Extraordinaria', id_acta='2'),
    ActaBase(activa=True, lenguaje='Català',
             fecha=now, tipo='Extraordinaria', id_acta='3'),
    ActaBase(activa=True, lenguaje='Français',
             fecha=now, tipo='Extraordinaria', id_acta='4'),
    ActaBase(activa=True, lenguaje='Chainese',
             fecha=now, tipo='Extraordinaria', id_acta='5'),
    ActaBase(activa=True, lenguaje='Deutsch',
             fecha=now, tipo='Extraordinaria', id_acta='6'),
    ActaBase(activa=False, lenguaje='Español',
             fecha=now, tipo='Extraordinaria', id_acta='7'),
    ActaBase(activa=False, lenguaje='English',
             fecha=now, tipo='Extraordinaria', id_acta='8'),
    ActaBase(activa=False, lenguaje='Català',
             fecha=now, tipo='Extraordinaria', id_acta='9'),
    ActaBase(activa=False, lenguaje='Français',
             fecha=now, tipo='Extraordinaria', id_acta='10'),
    ActaBase(activa=False, lenguaje='Chainese',
             fecha=now, tipo='Extraordinaria', id_acta='11'),
    ActaBase(activa=False, lenguaje='Deutsch',
             fecha=now, tipo='Extraordinaria', id_acta='12'),
    ActaBase(activa=True, lenguaje='Español',
             fecha=now, tipo='Extraordinaria', id_acta='13'),
    ActaBase(activa=True, lenguaje='English',
             fecha=now, tipo='Extraordinaria', id_acta='14'),
    ActaBase(activa=True, lenguaje='Català',
             fecha=now, tipo='Extraordinaria', id_acta='15'),
    ActaBase(activa=True, lenguaje='Français',
             fecha=now, tipo='Extraordinaria', id_acta='16'),
    ActaBase(activa=True, lenguaje='Chainese',
             fecha=now, tipo='Extraordinaria', id_acta='17'),
    ActaBase(activa=True, lenguaje='Deutsch',
             fecha=now, tipo='Extraordinaria', id_acta='18'),
    ActaBase(activa=False, lenguaje='Español',
             fecha=now, tipo='Extraordinaria', id_acta='19'),
    ActaBase(activa=False, lenguaje='English',
             fecha=now, tipo='Extraordinaria', id_acta='20'),
    ActaBase(activa=False, lenguaje='Català',
             fecha=now, tipo='Extraordinaria', id_acta='21'),
    ActaBase(activa=False, lenguaje='Français',
             fecha=now, tipo='Extraordinaria', id_acta='22'),
    ActaBase(activa=False, lenguaje='Chainese',
             fecha=now, tipo='Extraordinaria', id_acta='23'),
    ActaBase(activa=False, lenguaje='Deutsch',
             fecha=now, tipo='Extraordinaria', id_acta='24'),
    ActaBase(activa=True, lenguaje='Español',
             fecha=now, tipo='Extraordinaria', id_acta='25'),
    ActaBase(activa=True, lenguaje='English',
             fecha=now, tipo='Extraordinaria', id_acta='26'),
    ActaBase(activa=True, lenguaje='Català',
             fecha=now, tipo='Extraordinaria', id_acta='27'),
    ActaBase(activa=True, lenguaje='Français',
             fecha=now, tipo='Extraordinaria', id_acta='28'),
    ActaBase(activa=True, lenguaje='Chainese',
             fecha=now, tipo='Extraordinaria', id_acta='29'),
    ActaBase(activa=True, lenguaje='Deutsch',
             fecha=now, tipo='Extraordinaria', id_acta='30'),
    ActaBase(activa=False, lenguaje='Español',
             fecha=now, tipo='Extraordinaria', id_acta='31'),
    ActaBase(activa=False, lenguaje='English',
             fecha=now, tipo='Extraordinaria', id_acta='32'),
    ActaBase(activa=False, lenguaje='Català',
             fecha=now, tipo='Extraordinaria', id_acta='33'),
    ActaBase(activa=False, lenguaje='Français',
             fecha=now, tipo='Extraordinaria', id_acta='34'),
    ActaBase(activa=False, lenguaje='Chainese',
             fecha=now, tipo='Extraordinaria', id_acta='35'),
    ActaBase(activa=False, lenguaje='Deutsch',
             fecha=now, tipo='Extraordinaria', id_acta='36'),
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

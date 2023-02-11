from schemas.usuario import UsuarioLogin
from schemas.acta import ActaBase
from schemas.alumno import AlumnoBase
from datetime import datetime
import random  # TODO QUitar

now = datetime.utcfromtimestamp(random.randint(1675000000, 1675999999))

lista_acciones = [
    {"action_label": "Crear una convocatoria",
        "url": "actas/create"},  # Form vacio -> Post
    # Get todas las convocatorias
    {"action_label": "Listar acta", "url": "actas/list"},
    # Put fichero CSV para crear algo
    {"action_label": "Cargar CSV", "url": "alumnos/upload"},
    # Get todos los alumnos # Entiendo que para los correctores
    {"action_label": "Editar alumnos", "url": "alumnos/edit"},
    {"action_label": "Listar alumnos", "url": "alumnos/list"},
    {"action_label": "Listar convocatorias estados", "url": "alumnos/activo"}
]
fake_usuarios_DB = [
    UsuarioLogin(username="rick_sanchez", password="1234"),
    UsuarioLogin(username="morty_smith", password="1234"),
    UsuarioLogin(username="jerry_smith", password="1234")
]
fake_actas_DB = [
    ActaBase(estado=True, lenguaje='Español',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='1'),
    ActaBase(estado=True, lenguaje='English',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='2'),
    ActaBase(estado=True, lenguaje='Català',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='3'),
    ActaBase(estado=True, lenguaje='Français',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='4'),
    ActaBase(estado=True, lenguaje='Chainese',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='5'),
    ActaBase(estado=True, lenguaje='Deutsch',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='6'),
    ActaBase(estado=False, lenguaje='Español',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='7'),
    ActaBase(estado=False, lenguaje='English',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='8'),
    ActaBase(estado=False, lenguaje='Català',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='9'),
    ActaBase(estado=False, lenguaje='Français',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='10'),
    ActaBase(estado=False, lenguaje='Chainese',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='11'),
    ActaBase(estado=False, lenguaje='Deutsch',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='12'),
    ActaBase(estado=True, lenguaje='Español',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='13'),
    ActaBase(estado=True, lenguaje='English',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='14'),
    ActaBase(estado=True, lenguaje='Català',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='15'),
    ActaBase(estado=True, lenguaje='Français',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='16'),
    ActaBase(estado=True, lenguaje='Chainese',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='17'),
    ActaBase(estado=True, lenguaje='Deutsch',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='18'),
    ActaBase(estado=False, lenguaje='Español',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='19'),
    ActaBase(estado=False, lenguaje='English',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='20'),
    ActaBase(estado=False, lenguaje='Català',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='21'),
    ActaBase(estado=False, lenguaje='Français',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='22'),
    ActaBase(estado=False, lenguaje='Chainese',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='23'),
    ActaBase(estado=False, lenguaje='Deutsch',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='24'),
    ActaBase(estado=True, lenguaje='Español',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='25'),
    ActaBase(estado=True, lenguaje='English',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='26'),
    ActaBase(estado=True, lenguaje='Català',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='27'),
    ActaBase(estado=True, lenguaje='Français',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='28'),
    ActaBase(estado=True, lenguaje='Chainese',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='29'),
    ActaBase(estado=True, lenguaje='Deutsch',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='30'),
    ActaBase(estado=False, lenguaje='Español',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='31'),
    ActaBase(estado=False, lenguaje='English',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='32'),
    ActaBase(estado=False, lenguaje='Català',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='33'),
    ActaBase(estado=False, lenguaje='Français',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='34'),
    ActaBase(estado=False, lenguaje='Chainese',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='35'),
    ActaBase(estado=False, lenguaje='Deutsch',
             fecha=datetime.utcfromtimestamp(random.randint(1675000000, 1675999999)), tipo='Extraordinaria', id_acta='36'),
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

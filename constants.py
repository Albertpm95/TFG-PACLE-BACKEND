from schemas.usuario import UsuarioLogin

lista_acciones = [
    {"action_label": "Crear una convocatoria", "url": ""},  # Form vacio -> Post
    # Get todas las convocatorias
    {"action_label": "Listar convocatorias", "url": ""},
    # Put fichero CSV para crear algo
    {"action_label": "Cargar CSV", "url": ""},
    # Get todos los alumnos # Entiendo que para los correctores
    {"action_label": "Listar alumnos", "url": ""},
    {"action_label": "Listar convocatiroas activas", "url": ""}
]
fake_usuarios_DB = [
    UsuarioLogin(username="rick_sanchez", password="1234"),
    UsuarioLogin(username="morty_smith", password="1234"),
    UsuarioLogin(username="jerry_smith", password="1234")
]
fake_actas_DB = [
    {}
]

fake_alumnos_DB = [

]

from sqlalchemy import CheckConstraint, Column, String, Integer

from db.database import Base


class Rol(Base):
    __tablename__ = "roles"

    idRol = Column(Integer, primary_key=True)
    rol = Column(String, nullable=False, unique=True)
    
    __table_args__ = (
        CheckConstraint('roles.idRol NOT IN (1, 2, 3)', name='cannot_delete_role'),
    )

    roles_por_defecto = [
        {"idRol": 1, "rol": "Administrador"},
        {"idRol": 2, "rol": "Gestor"},
        {"idRol": 3, "rol": "Corrector"},
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for rol in self.roles_por_defecto:
            self.id = rol['idRol']
            self.rol = rol['rol']
            self._sa_instance_state.identity = None  # reiniciar el estado de la instancia para que se pueda agregar a la sesión

    def __repr__(self):
        return f"<Rol(roles.idRol={self.idRol}, roles.rol={self.rol})>"
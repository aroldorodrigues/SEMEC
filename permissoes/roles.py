from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {'ver_usuario': True, 'editar_usuario': True}
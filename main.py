"""
Proyecto python y MySql:
- Abrir asistente.
- Login o registro.
- Si elegimos registro, crear un usuario en la db.
- Si elegimos login, identificar el usuario.
- Crear, mostrar y eliminar notas.
"""

from usuarios import acciones as acc

print("""
 --------- Acciones Disponibles ---------

    - Registro
    - Login

""")

opt = acc.Acciones()

accion = input("¿Que quieres hacer?: ").upper()

if accion == "REGISTRO":
    opt.registro()

elif accion == "LOGIN":
    opt.login()


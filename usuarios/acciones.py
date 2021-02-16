from usuarios import usuario as usr

class Acciones:

    def registro(self):
        print("---- Registro de Usuario ----")

        nombre      = input("Nombre: ").upper()
        apellido    = input("Apellido: ").upper()
        email       = input("E-mail: ")
        passwd      = input("Password: ")

        user = usr.Usuario(nombre, apellido, email, passwd)
        registro = user.registrar()

        if registro[0] >=1:
            print(f"** Se ha registrado correctamente a {registro[1].nombre} {registro[1].apellido}")

        else:
            print(f"** imposible registrar a {registro[1].nombre} {registro[1].apellido}")

    def login(self):
        print("---- Inicio de Sesión ----")

        email       = input("E-mail: ")
        passwd      = input("Password: ")
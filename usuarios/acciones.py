from usuarios import usuario as usr
import notas.acciones
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

        try: 
            email       = input("E-mail: ")
            passwd      = input("Password: ")

            user = usr.Usuario('','',email, passwd)
            login = user.identificar()

            if email == str(login[3]):
                print("buen login")
                self.procimasAcciones(login)                
        
        except Exception as e:
            print("Credenciales incorrectas")

    def procimasAcciones(self, usuario):
        print("""\n
        --------- Administración de notas ---------

            - Crear nota (crear)
            - Mostrar notas (mostrar)
            - Eliminar notas (eliminar)
            - Salir (salir)

        """)

        accion = input("¿Que quieres hacer?: ").upper()
        opt = notas.acciones.Acciones()

        if accion == "CREAR":
            opt.crear(usuario)
            self.procimasAcciones(usuario)

        elif accion == "MOSTRAR":
            opt.mostrar(usuario)
            self.procimasAcciones(usuario)

        elif accion == "ELIMINAR":
            print("ELIMINAR nota")
            self.procimasAcciones(usuario)

        elif accion == "SALIR":
            print(f"\nGracias por usar notas. {usuario[1]} ten un exelente día!!!")
            exit()

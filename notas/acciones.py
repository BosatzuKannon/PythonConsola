import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"ok {usuario[1]}, vamos a crear una nota!")
        
        titulo      = input("Título: ")
        descripcion = input("Descripción: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)

        guardar = nota.guardar()

        if guardar[0] >=1:
            print(f"** Se ha registrado correctamente la nota: {nota.titulo}")

        else:
            print(f"** imposible registrar la nota: {nota.titulo}")

    
    def mostrar(self, usuario):
        print(f"\n------ Lista de notas de {usuario[1]} {usuario[2]} ------")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print(f"\nTítulo: {nota[2]}")
            print(f"Descripción: {nota[3]}")

    def borrar(self, usuario):
        print(f"ok {usuario[1]}, vamos a borrar una nota!")
        
        titulo      = input("Título: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >=1:
            print(f"** Se ha eliminado correctamente la nota: {nota.titulo}")

        else:
            print(f"** imposible eliminar la nota: {nota.titulo}")
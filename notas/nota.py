import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, usuario_id, titulo = "", descripcion = ""):
        self.usuario_id     = usuario_id
        self.titulo         = titulo
        self.descripcion    = descripcion

    def guardar(self):
        query = "INSERT INTO notas VALUES (null, %s, %s ,%s ,NOW())"

        nota= (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(query, nota)
        database.commit()

        return [cursor.rowcount, self]

    def listar(self):
        query = f"SELECT * FROM notas WHERE id_user = {self.usuario_id}"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def eliminar(self):
        query = f"DELETE FROM notas WHERE id_user = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        cursor.execute(query)
        database.commit()

        return [cursor.rowcount, self]
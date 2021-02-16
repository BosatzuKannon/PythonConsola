import datetime
import hashlib
from usuarios import conexion as db

connect = db.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellido, email, passwd):
        self.nombre     = nombre
        self.apellido   = apellido
        self.email      = email
        self.passwd     = passwd

    def registrar(self):
        
        fecha = datetime.datetime.now()
        cifrado = hashlib.sha256()
        cifrado.update(self.passwd.encode('utf8'))
        query = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        
        try:
            cursor.execute(query, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result
                

    def identificar(self):
        query = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        cifrado = hashlib.sha256()
        cifrado.update(self.passwd.encode('utf8'))

        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(query, usuario)
        result = cursor.fetchone()

        return result
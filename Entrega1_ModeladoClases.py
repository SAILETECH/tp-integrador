
from datetime import datetime

class Usuario:
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email
        self.__carpetas = [] 

    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email

    @property
    def carpetas(self):
        return self.__carpetas

    def crear_carpeta(self, nombre):
        carpeta = Carpeta(nombre)
        self.__carpetas.append(carpeta)
        return carpeta


class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__cuerpo = cuerpo
        self.__fecha = datetime.now()

    @property
    def remitente(self):
        return self.__remitente

    @property
    def destinatario(self):
        return self.__destinatario

    @property
    def asunto(self):
        return self.__asunto

    @property
    def cuerpo(self):
        return self.__cuerpo

    @property
    def fecha(self):
        return self.__fecha


class Carpeta:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def mensajes(self):
        return self.__mensajes

    def agregar_mensaje(self, mensaje):
        self.__mensajes.append(mensaje)

    def listar_mensajes(self):
        return [m.asunto for m in self.__mensajes]


class ServidorCorreo:
    def __init__(self):
        self.__usuarios = []

    def registrar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def enviar_mensaje(self, mensaje):

        for usuario in self.__usuarios:
            if usuario.email == mensaje.destinatario:
                inbox = next((c for c in usuario.carpetas if c.nombre == "Inbox"), None)
                if not inbox:
                    inbox = usuario.crear_carpeta("Inbox")
                inbox.agregar_mensaje(mensaje)
                return True
        return False

    def listar_usuarios(self):
        return [u.email for u in self.__usuarios]




if __name__ == "__main__":
    servidor = ServidorCorreo()

    u1 = Usuario("Elías", "elias@mail.com")
    u2 = Usuario("Ana", "ana@mail.com")

    servidor.registrar_usuario(u1)
    servidor.registrar_usuario(u2)

    msg = Mensaje("elias@mail.com", "ana@mail.com", "Hola", "¿Cómo estás?")
    servidor.enviar_mensaje(msg)

    print(u2.carpetas[0].listar_mensajes())  

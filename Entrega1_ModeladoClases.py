
from carpeta import Carpeta
from mensaje import Mensaje

class Usuario:


    def __init__(self, nombre: str, email: str):
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

    def crear_carpeta(self, nombre: str) -> Carpeta:
        carpeta = Carpeta(nombre)
        self.__carpetas.append(carpeta)
        return carpeta

    def listar_carpetas(self):
        return [c.nombre for c in self.__carpetas]

    def enviar_mensaje(self, destinatario: str, asunto: str, cuerpo: str, servidor):
   
        msg = Mensaje(self.email, destinatario, asunto, cuerpo)
        return servidor.enviar_mensaje(msg)

    def leer_mensajes(self, carpeta_nombre: str):
   
        carpeta = next((c for c in self.__carpetas if c.nombre == carpeta_nombre), None)
        if carpeta:
            return carpeta.listar_mensajes()
        return []
mensaje.py
python
Copiar código
from datetime import datetime

class Mensaje:

    def __init__(self, remitente: str, destinatario: str, asunto: str, cuerpo: str):
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
carpeta.py
python
Copiar código
from mensaje import Mensaje

class Carpeta:

    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__mensajes = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def mensajes(self):
        return self.__mensajes

    def agregar_mensaje(self, mensaje: Mensaje):
        self.__mensajes.append(mensaje)

    def listar_mensajes(self):
        return [m.asunto for m in self.__mensajes]
servidor.py
python
Copiar código
from carpeta import Carpeta
from mensaje import Mensaje
from usuario import Usuario

class ServidorCorreo:
  
    def __init__(self):
        self.__usuarios = []

    def registrar_usuario(self, usuario: Usuario):
        self.__usuarios.append(usuario)

    def enviar_mensaje(self, mensaje: Mensaje) -> bool:
    
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
main.py
python
Copiar código
from servidor import ServidorCorreo
from usuario import Usuario

if __name__ == "__main__":
    servidor = ServidorCorreo()

    u1 = Usuario("Elías", "elias@mail.com")
    u2 = Usuario("Ana", "ana@mail.com")

    servidor.registrar_usuario(u1)
    servidor.registrar_usuario(u2)

    u1.enviar_mensaje("ana@mail.com", "Hola", "¿Cómo estás?", servidor)
    print("Mensajes en la bandeja de entrada de Ana:", u2.leer_mensajes("Inbox"))

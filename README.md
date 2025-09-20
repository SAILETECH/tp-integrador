[README[1].md](https://github.com/user-attachments/files/22437999/README.1.md)
# 📧 Servicorreos

## 📌 Descripción
**Servicorreos** es un sistema de correo electrónico básico implementado en **Python**.  
Su objetivo es gestionar usuarios, mensajes y carpetas en un entorno que simula un cliente de correo electrónico simple.

## ✨ Características principales
- Registro de usuarios con nombre y correo.
- Envío de mensajes entre usuarios registrados.
- Organización de mensajes en carpetas (se crea automáticamente la carpeta *Inbox*).
- Consulta de mensajes recibidos en cada carpeta.
- Ejemplo de uso incluido en el bloque `if __name__ == "__main__":`.

## 🛠️ Diseño y Modelado
El sistema se desarrolló a partir de un **diagrama UML de clases**, donde se definieron las entidades principales y sus relaciones:

- **Usuario**: representa a una persona registrada, con nombre, email y sus carpetas asociadas.  
- **Carpeta**: organiza y almacena mensajes.  
- **Mensaje**: guarda remitente, destinatario, asunto, cuerpo y fecha de envío.  
- **ServidorCorreo**: administra los usuarios y se encarga de la entrega de mensajes.  


Título del Proyecto
Servicorreos – Cliente de Correo Electrónico en Python
________________________________________
1. Introducción
Este sistema implementa un cliente de correo electrónico básico.
Su propósito es modelar con Programación Orientada a Objetos (POO) las entidades principales de un correo electrónico: usuarios, mensajes, carpetas y un servidor que administra la entrega.
________________________________________
2. Alcance
•	Envío de mensajes entre usuarios registrados.
•	Recepción automática en la carpeta Inbox.
•	Creación y gestión de carpetas.
•	Listado de usuarios y mensajes.
________________________________________
3. Diseño del sistema
Clases principales
•	Usuario: gestiona sus carpetas y mensajes.
•	Carpeta: organiza mensajes.
•	Mensaje: almacena información de un correo.
•	ServidorCorreo: administra usuarios y realiza la entrega de mensajes.
Justificación del diseño
•	Se aplicó encapsulamiento para proteger atributos internos.
•	Cada clase tiene responsabilidad única.
•	El servidor funciona como mediador central → desacopla la lógica de usuarios.
•	Modularización: un archivo por clase, lo que mejora la mantenibilidad.
________________________________________
4. Diagrama UML
https://github.com/SAILETECH/tp-integrador/edit/master/README%5B1%5D.md


5. Futuras mejoras
•	Agregar autenticación de usuarios.
•	Implementar carpeta Enviados.
•	Permitir eliminar mensajes.
•	Guardar datos en una base de datos o archivos externos.

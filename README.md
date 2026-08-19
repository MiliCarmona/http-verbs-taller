# Servidor HTTP en Python

## Descripción

Este proyecto consiste en la implementación de un servidor HTTP utilizando Python y la interfaz **WSGI (Web Server Gateway Interface)** que proviene del módulo `wsgiref.simple_server`.

El servidor permite recibir solicitudes HTTP, identificar el método y la ruta solicitada, procesar datos enviados en formato JSON y responder utilizando los códigos de estado HTTP correspondientes.

La práctica tiene como objetivo comprender el funcionamiento básico de los métodos HTTP y su relación con las operaciones realizadas sobre los recursos de una API.

## Objetivos de este taller

- Comprender el funcionamiento básico del protocolo HTTP.
- Diferenciar los principales métodos HTTP y su propósito.
- Implementar un servidor HTTP básico utilizando Python.
- Procesar rutas y métodos HTTP recibidos por el servidor.
- Trabajar con datos con formatos JSON.
- Comprender el uso de códigos de estado HTTP.
- Ejecutar y verificar el funcionamiento del servidor mediante pruebas automatizadas.

## Tecnologías utilizadas

- Python3
- WSGI
- curl
- uv
- Bash (ejecución de las pruebas automatizadas)
- JSON (intercambio de información)

## Ejecución

Para iniciar el servidor, ejecutar:

uv run python server.py

Una vez iniciado correctamente, el servidor estará disponible en:

http://localhost:9292

El servidor permanecerá ejecutándose hasta que se interrumpa manualmente con:

Ctrl + C

## Pruebas

El proyecto incluye un script de pruebas automatizadas proporcionado para verificar el comportamiento del servidor. Primero se debe iniciar el servidor y mantenerlo ejecutándose. En una segunda terminal, ubicarse en el directorio del proyecto y ejecutar:

chmod +x test.sh

Luego:

./test-http-verbs.sh

El script realiza distintas solicitudes al servidor y verifica, entre otras cosas, los códigos de estado HTTP y el contenido de las respuestas. Al finalizar, se muestra un resumen con la cantidad de pruebas aprobadas y fallidas.

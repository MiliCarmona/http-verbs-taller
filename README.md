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

`uv run python server.py`

Una vez iniciado correctamente, el servidor estará disponible en:

`http://localhost:9292`

El servidor permanecerá ejecutándose hasta que se interrumpa manualmente con:

`Ctrl + C`

## Pruebas

El proyecto incluye un script de pruebas automatizadas proporcionado para verificar el comportamiento del servidor. Primero se debe iniciar el servidor y mantenerlo ejecutándose. En una segunda terminal, ubicarse en el directorio del proyecto y ejecutar:

`chmod +x test.sh`

Luego:

`./test-http-verbs.sh`

El script realiza distintas solicitudes al servidor y verifica, entre otras cosas, los códigos de estado HTTP y el contenido de las respuestas. Al finalizar, se muestra un resumen con la cantidad de pruebas aprobadas y fallidas.

## Consignas

En esta sección se encuentran las consignas correspondientes al taller.

**1)** Un único archivo Python (p. ej. `server.py`) que se ejecute con `uv run python server.py` y quede escuchando en `http://localhost:9292`.

**2)** En el README, una breve explicación con tus palabras de la diferencia entre `GET`, `POST`, `PATCH` y `DELETE`, y por qué `POST` no es idempotente.

## Respuestas de las consignas

**1)** Archivo `server.py` añadido en el repositorio.

**2)** Los métodos HTTP POST, PUT, PATCH, DELETE más utilizados son similares a las operaciones crear, actualizar, leer y eliminar en la bases de datos. Se tiene en cuenta los siguiente puntos clave:
- Crear una nueva tarea -> POST
- Leer las tareas -> GET
- Si la tarea existe, actualizar; de lo contrario, crear una nueva tarea -> PATCH
- Eliminar tarea -> DELETE

**GET**: Obtiene la tarea sin modificar el estado del servidor; es **idempotente**.

**POST**: Se utiliza para **crear** nuevas tareas en el servidor; no es **idempotente**. ¿Por qué no es idempotente? Porque cada ejecución de la misma solicitud puede generar un **estado diferente** en el servidor, creando **nuevas tareas** adicionales.
Si ejecutamos la misma petición **POST** tres veces con la tarea: `{"title": "Estudiar Python", "done": false}`:

**1)** El servidor crea `[{"id": 1, "title": "Estudiar Python", "done": false}]`, pero hasta ahí todo está perfecto.

**2)** El servidor vuelve a crear una tarea: `[{"id": 1, "title": "Estudiar Python", "done": false}, {"id": 1, "title": "Estudiar Python", "done": false}]`

**3)** Finalmente, al tercer POST vuelve a crear la misma tarea: `[{"id": 1, "title": "Estudiar Python", "done": false}, {"id": 1, "title": "Estudiar Python", "done": false}, {"id": 1, "title": "Estudiar Python", "done": false}]`

Eso significa que cada ejecución del POST **ejecuta un nuevo recurso**.

**PATCH**: Aplica modificaciones parciales a un recurso existente, enviando solo los campos que cambian.

**DELETE**: Elimina el recurso especificado; es **idempotente** (eliminar un recurso inexistente no genera error)

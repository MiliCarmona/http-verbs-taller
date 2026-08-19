import json

from wsgiref.simple_server import make_server

tasks = []
next_id = 1

def application(environ, start_response):

    global next_id

    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]

    print("Método:", method)
    print("Ruta:", path)

    #GET /tasks
    if method == "GET" and path == "/tasks":

        start_response(
            "200 OK",
            [("Content-Type", "application/json")]
        )

        response = json.dumps(tasks)

        return [response.encode("utf-8")]

    #GET /tasks/<id>
    if method == "GET" and path.startswith("/tasks/"):

        parts = path.split("/")
        task_id = int(parts[2])

        for task in tasks:

            if task["id"] == task_id:

                start_response(
                    "200 OK",
                    [("Content-Type", "application/json")]
                )

                response = json.dumps(task)

                return [response.encode("utf-8")]

        start_response(
            "404 Not Found",
            [("Content-Type", "text/plain")]
        )

        return [b"Tarea no encontrada"]

    if method == "POST" and path == "/tasks":

        length = int(environ.get("CONTENT_LENGTH", 0))

        body = environ["wsgi.input"].read(length)

        body = body.decode("utf-8")

        task = json.loads(body)

        task["id"] = next_id

        tasks.append(task)

        next_id += 1

        start_response(
            "201 Created",
            [("Content-Type", "application/json")]
        )

        response = json.dumps(task)

        return [response.encode("utf-8")]

    if method == "PUT" and path.startswith("/tasks/"):

        parts = path.split("/")

        task_id = int(parts[2])

        length = int(environ.get("CONTENT_LENGTH", 0))

        body = environ["wsgi.input"].read(length)

        body = body.decode("utf-8")

        new_task = json.loads(body)

        for task in tasks:

            if task["id"] == task_id:

                task["title"] = new_task["title"]

                start_response(
                    "200 OK",
                    [("Content-Type", "application/json")]
                )

                response = json.dumps(task)

                return [response.encode("utf-8")]

    if method == "PATCH" and path.startswith("/tasks/"):

        parts = path.split("/")

        task_id = int(parts[2])

        length = int(environ.get("CONTENT_LENGTH", 0))

        body = environ["wsgi.input"].read(length)

        body = body.decode("utf-8")

        changes = json.loads(body)

        for task in tasks:

            if task["id"] == task_id:

                if "title" in changes:
                    task["title"] = changes["title"]

                if "done" in changes:
                    task["done"] = changes["done"]

                start_response(
                    "200 OK",
                    [("Content-Type", "application/json")]
                )

                response = json.dumps(task)

                return [response.encode("utf-8")]

    if method == "DELETE" and path.startswith("/tasks/"):

        parts = path.split("/")

        task_id = int(parts[2])

        for task in tasks:

            if task["id"] == task_id:

                tasks.remove(task)

                start_response(
                    "200 OK",
                    [("Content-Type", "text/plain")]
                )

                return [b"Tarea eliminada"]

    start_response(
        "404 Not Found",
        [("Content-Type", "text/plain")]
    )

    return [b"Ruta no encontrada"]

server = make_server("localhost", 9292, application)

print("Servidor escuchando en http://localhost:9292")

server.serve_forever()
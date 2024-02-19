# Python parser with FastAPI and Celery\Request

Example of how to handle background processes with FastAPI, Celery, and Docker.

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to [http://localhost:8080/tasks](http://localhost:8004) to view the app.

Trigger a new task:

```sh
$ curl http://localhost:8080/tasks -H "Content-Type: application/json" --data '{"type": 0}'
```
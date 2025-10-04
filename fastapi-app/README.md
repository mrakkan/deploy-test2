# FastAPI Deploy Test

Minimal FastAPI app for deployment testing.

## Structure

```
fastapi-app/
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

## Build locally

```
docker build -t fastapi-test ./fastapi-app
docker run -d -p 3000:80 fastapi-test
```

Open `http://localhost:3000/` and `http://localhost:3000/health`.

## Use with the platform

- Set `Dockerfile Path` to `fastapi-app/Dockerfile`.
- Leave `Exposed Port` empty to auto-assign a host port.
- Container listens on `PORT` env (default `80`). If you prefer `8000`, change `ENV PORT=8000` and `EXPOSE 8000`, then set `container_port = 8000` in the project.
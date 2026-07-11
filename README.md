# DevOps Assignment App (Python/Flask)

A simple Flask web app built for the DevOps Engineer technical assignment.
Includes a health-check endpoint, a JSON API endpoint, and a CPU-work endpoint
(useful later for load testing).

## Run locally (no Docker)

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit: http://localhost:5000

## Run locally with Docker

```bash
docker build -t devops-app .
docker run -p 5000:5000 devops-app
```

Visit: http://localhost:5000

## Endpoints

| Route | Description |
|---|---|
| `/` | Home page |
| `/health` | Health check (status, hostname, uptime) |
| `/api/info` | JSON info + visit counter |
| `/api/compute` | CPU-heavy endpoint, useful for load testing |
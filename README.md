# InterviewIQ

InterviewIQ is an AI-powered mock interview and performance assessment system.

## Prerequisites

- Docker Desktop
- Git

## Setup Instructions

1. Clone the repository.
2. Open the project folder in a terminal.
3. Create a `.env` file using `.env.example` and configure the required environment variables.
4. Start the backend and PostgreSQL database:

```bash
docker compose up --build
```

## API Endpoints

- `GET /health` — Checks whether the API is running.
- `GET /health/db` — Checks the database connection.
- `/docs` — Opens the FastAPI interactive API documentation.

## Stop the Services

```bash
docker compose down
```

## Technology Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker Compose
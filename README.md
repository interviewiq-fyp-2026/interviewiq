# InterviewIQ

InterviewIQ is an AI-powered mock interview and performance assessment system.

Final year project, PUCIT, University of the Punjab.

- Team: Kinza Abrar (lead), Arooj Qayyum, Zunaira Ghulam Nabi
- Supervisor: Sir Imran Bin Naseer

## Folders

- backend - API and database
- frontend - web app and camera panel
- agents - AI agents and orchestration
- data - dataset pipeline and question bank
- docs - requirements and design documents

## Prerequisites

- Git
- Docker Desktop
- Windows PowerShell (for Windows users)

## Setup Instructions

### 1. Clone the Repository

Clone the InterviewIQ repository and open the project folder in VS Code.

### 2. Start Docker Desktop

Open Docker Desktop and wait until the Docker engine is running before executing the commands below.

### 3. Configure Environment Variables

In Windows PowerShell, run the following command from the project root folder to create `.env` from `.env.example`:

```powershell
Copy-Item .env.example .env
```

In Git Bash, macOS or Linux, use: `cp .env.example .env`

If a `.env` file already exists, do not overwrite it. Check its configuration instead.

Make sure the required PostgreSQL environment variables are configured in `.env`.

### 4. Build and Start the Services

Run the following command from the project root folder:

```powershell
docker compose up --build -d
```

This starts the FastAPI backend and PostgreSQL database.

### 5. Verify the Services

Open these URLs in your browser:

- API health: http://localhost:8000/health
- Database health: http://localhost:8000/health/db
- Interactive API documentation: http://localhost:8000/docs

Expected responses:

- `/health` returns `{"status":"ok"}`
- `/health/db` returns `{"database":"ok"}`

### 6. Check Container Status

Run:

```powershell
docker compose ps
```

The API container should be running, and the database container should be healthy.

## Stop the Services

To stop the containers without deleting the database volume, run:

```powershell
docker compose down
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Checks whether the API is running |
| GET | `/health/db` | Checks the database connection |
| GET | `/docs` | Opens the FastAPI interactive API documentation |

## Technology Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose

## How we work

- Never push directly to main or dev.
- One branch per ticket: feature/<ticket-id>-<short-name>
- Open a pull request into dev; a teammate must approve before merging.
- Commit messages: feat, fix, test or docs, a colon, then the ticket ID, for example
  feat: T07 add health endpoint
- Never commit passwords, API keys, videos or audio.
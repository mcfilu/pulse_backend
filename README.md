# Pulse.io BackEnd app

This project is a FastAPI application that serves as a backend for the Pulse.io Full-Stack Application. It interacts with an external regres.in API to fetch user data and provides endpoints to retrieve this data.

## Project Structure
```markdown
.
├── app
│   ├── __init__.py
│   ├── crud
│   │   └── __init__.py
│   ├── db
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── schemas
│   │   └── __init__.py
│   ├── main.py
│   ├── routers
│   │   ├── __init__.py
│   │   └── users.py
│   └── helpers
│       ├── __init__.py
│       └── users.py
├── tests
│   ├── __init__.py
│   ├── users
│   │   ├── __init__.py
│   │   ├── test_decorators.py
│   │   ├── test_helpers.py
├── .gitignore
├── requirements.txt
├── Dockerfile
├── compose.yaml
└── README.md
```
app: Contains the main application code.

main.py: Entry point of the FastAPI application.

models: Future proof folder, place to put the SQLAlchemy models.

routers: Contains router modules defining API endpoints, structures functionality into logical/business order.

helpers: Contains helper functions used in the routers.

schemas: Future proof folder, place to put the Pydantic Schemas in the future.

crud: Future proof folder, place to put all the functions responsible for handling crud operations between routets and ORM.

db: Future proof folder, place to config the db, set the engine, session, base class etc.

tests: Contains unit and integration tests for the application.

requirements.txt: Lists dependencies required to run the application.

Dockerfile: Defines the Docker image for the application.

compose.yaml: Configures services for running the application and any dependencies.

README.md: This file, providing information about the project.

# Available Endpoints
GET /: Send the universal message about where the docs are available, helper endpoint for lost developer, as long as there isnt any functionality on that url!

GET /users/{user_id}: Retrieves user data from an external API based on the provided user ID.
How It Works
The application fetches user data from an external API (reqres.in) and exposes an endpoint to retrieve this data. When a request is made to /users/{user_id}, the application fetches the corresponding user data from the external API, processes it, and returns it to the client. Error handling is implemented to deal with invalid requests or errors from the external API.



# Running the Application
## Prerequisites
-Python3.10

-Docker

## Setup
Clone the repository:

```bash
Copy code:
git clone https://github.com/mcfilu/pulse_backend
cd pulse_backend
```

## Running with Docker
You can also run the application using Docker:

```bash
Copy code:
docker compose up -d --build
```
The application will be accessible at http://localhost:8080.

## Running Locally
You can run the application locally using uvicorn:

Install dependencies:

```bash
Copy code:
pip install -r requirements.txt
```

```bash
Copy code:
uvicorn app.main:app --reload
```
The application will be accessible at http://localhost:8000.

## Testing

In order to run the written unit and integration tests, utilise pytest framework.

-Inisde running Docker Container, open terminal and run "pytest".
-Run pytest in your terminal that uses the appropriate environment.




# Shahzeb To-Do API

A simple To-Do List REST API built with Python and Flask.

This project was created as a DevOps & Cloud Internship take-home challenge.

## Features

* Add a task
* List all tasks
* Mark a task as completed
* Run the application locally
* Run the application using Docker
* Automatically build the Docker image using GitHub Actions

## Technology Used

* Python
* Flask
* Docker
* GitHub
* GitHub Actions

## Project Structure

```text
shahzeb-todo-api/
├── .github/
│   └── workflows/
│       └── docker-build.yml
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Requirements

Before running the project, make sure you have:

* Python 3
* pip
* Docker
* Git

## Step 1: Clone the Repository

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/shahzeb-todo-api.git
```

Go into the project directory:

```bash
cd shahzeb-todo-api
```

## Step 2: Create a Python Virtual Environment

Create the virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

## Step 3: Install Dependencies

Install the required Python package:

```bash
pip install -r requirements.txt
```

## Step 4: Run the Application

Start the Flask application:

```bash
python3 app.py
```

The application will start on:

```text
http://localhost:5000
```

## API Endpoints

### 1. Add a Task

**Method:** `POST`

**Endpoint:**

```text
/tasks
```

Example:

```bash
curl -X POST http://localhost:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Learn Docker"}'
```

Example response:

```json
{
    "done": false,
    "id": 1,
    "title": "Learn Docker"
}
```

The task is added to the in-memory task list with a unique ID.

---

### 2. List Tasks

**Method:** `GET`

**Endpoint:**

```text
/tasks
```

Example:

```bash
curl http://localhost:5000/tasks
```

Example response:

```json
[
    {
        "done": false,
        "id": 1,
        "title": "Learn Docker"
    }
]
```

This endpoint returns all tasks currently stored in memory.

---

### 3. Mark a Task as Done

**Method:** `PATCH`

**Endpoint:**

```text
/tasks/<id>/done
```

Example:

```bash
curl -X PATCH http://localhost:5000/tasks/1/done
```

Example response:

```json
{
    "done": true,
    "id": 1,
    "title": "Learn Docker"
}
```

This changes the selected task's `done` value from `false` to `true`.

## Step 5: Run with Docker

Build the Docker image:

```bash
docker build -t shahzeb-todo-api .
```

Run the Docker container:

```bash
docker run -p 5000:5000 shahzeb-todo-api
```

The application will now be available at:

```text
http://localhost:5000
```

Test the API:

```bash
curl http://localhost:5000/tasks
```

You can also add a task:

```bash
curl -X POST http://localhost:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Docker Test"}'
```

## Step 6: GitHub Actions

This project includes a GitHub Actions workflow:

```text
.github/workflows/docker-build.yml
```

The workflow runs automatically whenever code is pushed to the GitHub repository.

The workflow performs these steps:

1. Checks out the repository code.
2. Sets up the GitHub Actions runner.
3. Builds the Docker image.
4. Reports whether the Docker build was successful.

The workflow only builds the Docker image. It does not deploy the application.

## Step 7: GitHub Repository

Initialize Git:

```bash
git init
```

Add the project files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Initial To-Do API"
```

Set the main branch:

```bash
git branch -M main
```

Add the GitHub repository:

```bash
git remote add origin https://github.com/YOUR_USERNAME/shahzeb-todo-api.git
```

Push the project:

```bash
git push -u origin main
```

After pushing, open the **Actions** tab on GitHub to see the Docker build workflow.

## Data Storage

The application uses in-memory storage.

Tasks are stored in a Python list while the application is running.

No database is used because persistent storage was not required for this challenge.

When the application is restarted, the tasks are cleared.

## Reflection

I kept the application simple because the challenge only required three basic API endpoints.

I chose Flask because it is lightweight and easy to understand for a small REST API.

I used in-memory storage because a real database was not required by the challenge.

The main learning point was connecting the application with Docker and GitHub Actions.

The Dockerfile packages the application and its dependency into a container, while GitHub Actions automatically verifies that the Docker image can be built successfully after every push.

If I had another day, I would improve the project by adding a database for persistent storage, automated API tests, input validation, better error handling, and Docker image publishing.

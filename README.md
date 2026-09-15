# Shahzeb To-Do API

A simple To-Do List API built with Python and Flask.

## Endpoints

### Add a task

POST /tasks

Example:

```bash
curl -X POST http://localhost:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Learn Docker"}'

from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
next_id = 1


@app.route("/tasks", methods=["POST"])
def add_task():
    global next_id

    data = request.get_json()

    task = {
        "id": next_id,
        "title": data["title"],
        "done": False
    }

    tasks.append(task)
    next_id += 1

    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(tasks)


@app.route("/tasks/<int:task_id>/done", methods=["PATCH"])
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return jsonify(task)

    return {"error": "Task not found"}, 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

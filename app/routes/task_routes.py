from flask import Blueprint, request
from app.models.task import Task
from app.db import db

tasks_bp = Blueprint("task_bp", __name__, url_prefix="/tasks")

@tasks_bp.post("")
def create_task():
    request_body = request.get_json()
    title = request_body["title"]
    description = request_body["description"]
    completed_at = request_body["completed_at"]

    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()

    response = new_task.to_dict()
    return response, 201

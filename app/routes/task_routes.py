from flask import Blueprint, request, abort, make_response, Response
from app.models.task import Task
from app.db import db

tasks_bp = Blueprint("task_bp", __name__, url_prefix="/tasks")

@tasks_bp.post("")
def create_task():
    request_body = request.get_json()

    if "title" not in request_body or "description" not in request_body:
        return {"details": "Invalid data"}, 400

    title = request_body["title"]
    description = request_body["description"]
    completed_at = request_body.get("completed_at", None)
    is_complete = request_body.get("is_complete", False)

    new_task = Task(title=title, description=description, is_complete=is_complete)
    db.session.add(new_task)
    db.session.commit()

    response = {"task": new_task.to_dict()}
    return response, 201


@tasks_bp.get("")
def get_all_tasks():
    
    sort_order = request.args.get("sort")

    if sort_order == "asc":
        query = db.select(Task).order_by(Task.title.asc())
    elif sort_order == "desc":
        query = db.select(Task).order_by(Task.title.desc())
    else:
        query = db.select(Task).order_by(Task.id)
    
    tasks = db.session.scalars(query)
    tasks_response = [task.to_dict() for task in tasks]

    return tasks_response


@tasks_bp.get("/<task_id>")
def get_single_task(task_id):

    task = validate_task(task_id)

    return {"task": task.to_dict()}

@tasks_bp.put("/<task_id>")
def update_task(task_id):
    task = validate_task(task_id)
    request_body = request.get_json()

    task.title = request_body["title"]
    task.description = request_body["description"]
    task.completed_at = request_body.get("completed_at", None)
    task.is_complete = request_body.get("is_complete", False)

    db.session.commit()

    return {"task": task.to_dict()}


@tasks_bp.delete("/<task_id>")
def delete_task(task_id):
    task = validate_task(task_id)

    db.session.delete(task)
    db.session.commit()

    return {"details": f'Task {task_id} "Go on my daily walk 🏞" successfully deleted'}


def validate_task(task_id):
    try:
        task_id = int(task_id)
    except:
        response = {"message": f"Task id {task_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Task).where(Task.id == task_id)
    task = db.session.scalar(query)
    
    if not task:
        response = {"message": f"Task {task_id} not found"}
        abort(make_response(response, 404))

    return task

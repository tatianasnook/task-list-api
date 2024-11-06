from flask import Blueprint, request
from app.models.goal import Goal
from app.db import db
from app.routes.route_utilities import validate_model

bp = Blueprint("goal_bp", __name__, url_prefix="/goals")

@bp.post("")
def create_goal():
    request_body = request.get_json()

    if "title" not in request_body:
        return {"details": "Invalid data"}, 400

    title = request_body["title"]

    new_goal = Goal(title=title)
    db.session.add(new_goal)
    db.session.commit()

    return {"goal": new_goal.to_dict()}, 201
    

@bp.get("")
def get_all_goals():
    query = db.select(Goal).order_by(Goal.id)
    goals = db.session.scalars(query)

    return [goal.to_dict() for goal in goals]
    

@bp.get("/<goal_id>")
def get_single_goal(goal_id):

    goal = validate_model(Goal, goal_id)
    return {"goal": goal.to_dict()}


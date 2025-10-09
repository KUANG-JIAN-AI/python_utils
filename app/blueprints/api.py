from flask import Blueprint, jsonify
from app.controllers.admin import signin, signup

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/signup", methods=["POST"])
def api_signup():
    return jsonify(signup())


@api_bp.route("/signin", methods=["POST"])
def api_signin():
    return jsonify(signin())

from flask import Blueprint, jsonify, render_template

main_bp = Blueprint("main", __name__)
@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/user")
def user_tpl():
    return render_template("user.html")

@main_bp.route("/signin")
def signin_tpl():
    return render_template("signin.html")

@main_bp.route("/signup")
def signup_tpl():
    return render_template("signup.html")
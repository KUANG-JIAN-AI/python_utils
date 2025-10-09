from flask import Blueprint, jsonify, render_template

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def index():
    return render_template("index.html")


@index_bp.route("/user")
def user_tpl():
    return render_template("user.html")


@index_bp.route("/signin")
def signin_tpl():
    return render_template("signin.html")


@index_bp.route("/signup")
def signup_tpl():
    return render_template("signup.html")

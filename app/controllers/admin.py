import secrets
from flask import current_app, request

from app.models.admin import Admins, db
from app.utils import dataful, errorful, md5, successful


def signup():
    """执行注册

    Returns:
        string: 注册成功信息
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return errorful(code=100100, msg="账号或密码为空")

    with current_app.app_context():
        admin = Admins.query.filter_by(username=username).first()
        if admin is not None:
            return errorful(code=100200, msg="账号已存在")

    admin = Admins(username=username)
    # 加密密码
    admin.set_password(password)
    db.session.add(admin)
    db.session.commit()

    return successful(msg="注册成功")


def signin():
    """执行登录

    Returns:
        object: 登录信息
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return errorful(code=100100, msg="账号或密码为空")

    with current_app.app_context():
        admin = Admins.query.filter_by(username=username).first()

        if admin is None:
            return errorful(code=100400, msg="账号不存在")

        if admin.check_password(password):
            # 生成登录 token
            admin.access_token = secrets.token_hex(32)
            db.session.commit()

            return dataful(msg="登录成功", data=admin.to_dict())
        else:
            return errorful(code=100300, msg="密码错误")

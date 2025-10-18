import hashlib
import os
import secrets

from flask import current_app, request, url_for
from werkzeug.utils import secure_filename


def dataful(msg="success", data={}):
    return {"code": 200, "msg": msg, "data": data}


def successful(msg="success"):
    return {"code": 200, "msg": msg}


def errorful(code=400, msg="error"):
    return {"code": code, "msg": msg}


def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def format_datetime(dt):
    if not dt:
        return None
    return dt.strftime("%Y-%m-%d %H:%M:%S")


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_image():
    # 调整这里的 key 名称以匹配前端发送的 field name（例如 'file' 或 'avatar'）
    file = request.files.get("file") or request.files.get("avatar")
    if not file:
        return {"error": "no file provided"}

    if file.filename == "":
        return {"error": "empty filename"}

    if not allowed_file(file.filename):
        return {"error": "file type not allowed"}

    # 保留扩展名但不要使用原始文件名（防止冲突）
    ext = os.path.splitext(secure_filename(file.filename))[
        1
    ].lower()  # 包含点，如 ".png"
    if ext == "":
        return {"error": "no extension"}

    # 生成随机文件名：比如 16 个 hex 字符
    random_name = secrets.token_hex(16) + ext  # 32-hex 长度，足够随机
    # 或者用 uuid: import uuid; random_name = uuid.uuid4().hex + ext

    # 取到项目根目录下的 static/uploads，确保目录存在
    upload_folder = os.path.join(current_app.root_path, "static", "uploads")
    os.makedirs(upload_folder, exist_ok=True)  # 如果不存在就创建

    filepath = os.path.join(upload_folder, random_name)

    # 保存文件
    file.save(filepath)

    # 返回可以被前端直接使用的 URL（Flask url_for）
    file_url = url_for("static", filename="uploads/" + random_name, _external=False)
    return {"url": file_url, "filename": random_name}

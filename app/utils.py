import hashlib


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

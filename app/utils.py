def dataful(msg="success", data=[]):
    return {"code": 200, "msg": msg, "data": data}


def successful(msg="success"):
    return {"code": 200, "msg": msg}


def errorful(code=400, msg="error"):
    return {"code": code, "msg": msg}

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 数据库实例


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")  # 加载配置

    db.init_app(app)  # 初始化数据库

    # 注册蓝图
    # 注册 index 路由
    from .blueprints.index import index_bp

    app.register_blueprint(index_bp)

    # 注册 api 路由
    from .blueprints.api import api_bp

    app.register_blueprint(api_bp)

    return app

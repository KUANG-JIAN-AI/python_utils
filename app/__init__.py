from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 数据库实例

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")  # 加载配置

    db.init_app(app)  # 初始化数据库

    # 注册蓝图
    from .routes.router import main_bp
    app.register_blueprint(main_bp)

    return app
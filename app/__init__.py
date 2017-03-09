from flask import Flask
from config import config
import time,threading


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def basic_thread(app):
    basic=app.config["BASIC"]
    basic_t=threading.Thread(target=basic.run,name="basic_thread")
    try:
        basic_t.start()
    except Exception as e:
        print("app/__init__.py-basic_thread error")
    finally:
        basic_t.join()


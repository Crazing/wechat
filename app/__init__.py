from flask import Flask
from config import config
import time,threading
from .basic import Basic


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def basic_thread_start(app):
    basic=app.config["BASIC"]
    basic_t=threading.Thread(target=basic.run,name="basic_thread")
    app.config["BASIC_T"]=basic_t
    basic_t.start()

def basic_thread_join(app):
    basic_t=app.config["BASIC_T"]
    if not basic_t:
        return
    Basic.basic_end=False
    basic_t.join()
    
    

from app.basic import Basic
from app.menu import menu
from app.menu_config import postJson
class Config:
    BASIC=Basic() 
    MENU=menu()
    POSTJSON=postJson
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    pass 
config={
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}

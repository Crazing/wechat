from app.basic import Basic
from app.menu import Menu
from app.menu_config import postJson
class Config:
    BASIC=Basic() 
    MENU=Menu()
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

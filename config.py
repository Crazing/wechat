class Config:
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    pass 
config={
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}

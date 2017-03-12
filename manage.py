#!/usr/bin/env python3
import os
from app import create_app,basic_thread_start,basic_thread_join,menu_create
from app.basic import Basic
from app.media import Media
from app.material import Material
from app.material_config import news
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
if __name__ == '__main__':
    basic_thread_start(app)
   # materia=Material()
   # imgpath=os.path.abspath('.')+'/app/static/image/fengjing.jpg'
   # materia.upload(Basic.get_access_token(),imgpath)
   # materia.add_news(Basic.get_access_token(),news)
    menu_create(app)
    #app.run()
    app.run(host='10.104.185.229',port=80)
    basic_thread_join(app)


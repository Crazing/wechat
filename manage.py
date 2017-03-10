#!/usr/bin/env python3
import os
from app import create_app,basic_thread_start,basic_thread_join,menu_create
from app.basic import Basic
from app.media import Media
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
if __name__ == '__main__':
    basic_thread_start(app)
    menu_create(app)
    #app.run()
    app.run(host='10.104.185.229',port=80)
    basic_thread_join(app)


#!/usr/bin/env python3
import os
from app import create_app,basic_thread_start,basic_thread_join
from app.basic import Basic
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
if __name__ == '__main__':
    basic_thread_start(app)
    app.run(host='10.104.185.229',port=80,debug=True)
    basic_thread_join(app)


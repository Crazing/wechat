#!/usr/bin/env python3
import os
from app import create_app,basic_thread
from app.basic import Basic
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
basic_thread(app)
print(Basic.get_access_token())
if __name__ == '__main__':
    app.run(host='10.104.185.229',port=80,debug=True)


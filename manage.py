#!/usr/bin/env python3
import os
from app import create_app
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
if __name__ == '__main__':
    app.run(host='10.104.185.229',port=80,debug=True)


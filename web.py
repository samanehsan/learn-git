""" Heroku/Python Quickstart: https://blog.heroku.com/archives/2011/9/28/python_and_django"""

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Hello from the SPARK learn-a-thon!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

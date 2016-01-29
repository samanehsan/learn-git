""" 
Heroku/Python Quickstart: 
https://blog.heroku.com/archives/2011/9/28/python_and_django
"""

import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    name = 'poo'
    instagram_pics = [1, 2, 3, 4, 5, 6, 7]  #  instagram_pics()
    twitter_pics = [1, 2, 3]  #  twitter_pics()
    return render_template(
        'home.html', name=name, 
        instagram_pics=instagram_pics, 
        twitter_pics=twitter_pics,
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, debug=True)

'''
HOW TO SET UP FLASK

1) In terminal
    1.1) set FLASK_APP=app.py
    1.2) set FLASK_ENV=development
2) Run Flask - in terminal: flask run

pip install pymongo[srv]

'''

'''
WHAT I HAVE DONE TO MAKE THE TEMPLATE WORK

- Made 2 folders: "templates" and "static"
- I have inserted the "index.html" file in "templates"
- I have inserted all dependency folders: css, images, js and scripts in "static"
- I have created a Python file: app.py
- In index file, I have:
    - Added url_open when having a path refering to one of the 4 dependency folder
    - Removed version referencing
'''


import datetime
from flask import Flask, render_template, request, send_from_directory, url_for

def create_app():

    # Has to be this name 
    # Then deployment mechanism will only deploy this app and MongoClient ONCE

    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html")
        # return send_from_directory('', 'index.html')

    return app

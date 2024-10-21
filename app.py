from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS

app = Flask(__name__)
load_dotenv

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def hello_world():
    return "hello , world"

if __name__ == '__main__':
    app.run()
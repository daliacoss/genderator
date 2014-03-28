from flask import Flask
import genderator.config as config

app = Flask(__name__)
app.config.from_pyfile("config.py")

class WebFactionMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = config.environ
        return self.app(environ, start_response)

app.wsgi_app = WebFactionMiddleware(app.wsgi_app)

import genderator.models
import genderator.views
#@app.route("/")
#def hello():
#    return "Hello World!"



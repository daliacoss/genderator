from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config.py")

class WebFactionMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = 'genderator'
        return self.app(environ, start_response)

app.wsgi_app = WebFactionMiddleware(app.wsgi_app)

import genderator.views
import genderator.models
#@app.route("/")
#def hello():
#    return "Hello World!"



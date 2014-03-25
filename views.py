from genderator import app

@app.route("/")
def index():
    return "Hello World!"

@app.route("/genderate")
def genderate():
	return "genderator coming soon..."

#@app.errorhandler(404)
#def error404(e):
#	return "Page not found", 200

import random
from flask import jsonify, request, render_template, url_for
from genderator import app
from genderator.models import *
from sqlalchemy import func

class RStripped(object):
	def __init__(self, string, charsToStrip):
		self.charsToStrip = charsToStrip
		self.string = string.rstrip(self.charsToStrip)

	def __get__(self, instance, owner):
		return self.string

	def __set__(self, instance, value):
		#set string to string.rstrip()
		self.string = value.string.rstrip(self.charsToStrip)

class URL(object):
	
	def __init__(self, root=""):
		self.root = root

	@property
	def root(self):
		return self._root

	@root.setter
	def root(self, value):
		self._root = value.rstrip("/")

	# def __getattr__(self, name):
	# 	print "hi"
	# 	return 

class Url(object):
	def __init__(self, url, path=None):
		self.url = url
		if path:
			path.append(self.url)
			self.path = path
		else:
			self.path = [self.url]

a = Url("")
a.genderate = Url("genderate", a.path)

urls = URL("")
urls.genderate = URL("genderate/")
urls.genderate.get_random_gender = URL("get_random_gender")

#genderate/get_random_gender

print urls.genderate.root
print urls

@app.route("/")
def index():
    return "Hello World!"

@app.route("/genderate/")
def genderate():
	return render_template("genderate.html")

@app.route("/genderate/get_random_gender/")
def get_random_gender():
	g = getRandomGender()
	return jsonify(genderId=g.id, genderName=g.name, genderPronounSetId=g.pronoun_set_id)

#@app.errorhandler(404)
#def error404(e):
#	return "Page not found", 200

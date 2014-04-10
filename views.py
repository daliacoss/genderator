import random
from flask import jsonify, request, render_template, url_for, redirect
from genderator import app
from genderator.models import *
from sqlalchemy import func

class URL(object):
	
	def __init__(self, url=""):
		self.url = url

	@property
	def urlf(self):
		return self._url + "/"

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, value):
		self._url = value.rstrip("/")

	def newURL(self, url, safeSlashes=True):
		"""create a new local URL, relative to this URL"""

		if type(url) == str:
			if safeSlashes:
				url = url.lstrip("/")
			setattr(self, url, URL(self.url + "/" + url))
		else:
			raise TypeError("url must be string")

urls = URL("")
urls.newURL("settings")
urls.newURL("genderate")
urls.genderate.newURL("get_random_gender")
urls.genderate.newURL("get_all_genders")

@app.route("/", methods=["GET", "POST"])
def index():
	return redirect("/settings")

@app.route(urls.settings.urlf, methods=["GET", "POST"])
def editprofile():
	return render_template("settings.html")

@app.route(urls.genderate.urlf)
def genderate():
	return render_template("genderate.html", gender=getRandomGender())

@app.route(urls.genderate.get_all_genders.urlf)
def get_all_genders():
	gcollection = [g.toDict() for g in getGenders({})]
	return jsonify(genders=gcollection)
	#return gcollection[0]

@app.route(urls.genderate.get_random_gender.urlf)
def get_random_gender():
	g = getRandomGender()
	return jsonify(genderId=g.id, genderName=g.name, genderPronounSetId=g.pronoun_set_id)

#@app.errorhandler(404)
#def error404(e):
#	return "Page not found", 200

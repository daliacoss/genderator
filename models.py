from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from genderator import app

db = SQLAlchemy(app)
	
class Gender(db.Model):
	__tablename__ = "genders"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150), unique=True, index=False)
	pronoun_set_id = db.Column(db.Integer, db.ForeignKey("pronoun_sets.id"))

	def __init__(self, name, pronoun_set_id=None):
		self.name = name
		self.pronoun_set_id = pronoun_set_id

class PronounSet(db.Model):
	__tablename__ = "pronoun_sets"

	id = db.Column(db.Integer, primary_key=True)
	pronoun_subject = db.Column(db.String(30))
	pronoun_object = db.Column(db.String(30))
	pronoun_possessive = db.Column(db.String(30))
	description = db.Column(db.String(80))

	def __init__(self, pronoun_subject, pronoun_object, pronoun_possessive, description=""):
		self.pronoun_subject = pronoun_subject
		self.pronoun_object = pronoun_object
		self.pronoun_possessive = pronoun_possessive
		self.description = description

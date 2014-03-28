import random
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import func
from genderator import app

db = SQLAlchemy(app)
pronounIdFemale = 1
pronounIdMale = 2
pronounIdNeutral = 3
defaultPronounId = pronounIdNeutral #traditionally neutral - they,them,their

class Gender(db.Model):
	__tablename__ = "genders"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150), unique=True, index=False)
	pronoun_set_id = db.Column(db.Integer, db.ForeignKey("pronoun_sets.id"))

	def __init__(self, name, pronoun_set_id=defaultPronounId):
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

def getGenderQuery(name, database=db):
	return database.session.query(Gender).filter_by(name=name)

def getGender(name, database=db):
	genders = getGenderQuery(name, database).all()
	if len(genders):
		return genders[0]

def getRandomGender(database=db):
	highest = database.session.query(func.max(Gender.id)).scalar();
	#randint is inclusive-inclusive
	index = random.randint(1, highest)
	return db.session.query(Gender).filter_by(id=index).all()[0]

"""update gender entry using dict of values"""
def updateGender(name, values, database=db):
	getGenderQuery(name, database).update(values)
	database.session.commit()

def insertGenderFromValues(name, pronounSetId=defaultPronounId, database=db):
	if not getGender(name, database):
		database.session.add(Gender(name, pronounSetId))
		database.session.commit()

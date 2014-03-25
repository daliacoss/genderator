from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from genderator import app

db = SQLAlchemy(app)

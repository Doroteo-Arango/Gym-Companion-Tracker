# Create database models
# From current package(website folder) import db object
from . import db
# Custom class that will give our user object something specific for flask login
# It will help users log in
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # SQLAlchemy will take care of defining a date & time
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Associate a note with a user
    # Use a foreign key - a key in a db table that references an id to another db column
    # One-to-many relationship where one single parent object might have multiple children objects associated
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

# Store all users in a schema that looks like this:
class User(db.Model, UserMixin):
    # Primary key is a unique identifier in the form of an integer, which is used in 'user_id' above ^^^
    id = db.Column(db.Integer, primary_key=True)
    # Email will be a string of max length 150. No user can have the same email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Tell Flask & SQLAlchemy that every time a note is created, add into 'notes' that note id
    # It will essentially be a list that stores the notes that a user has created
    notes = db.relationship("Note")
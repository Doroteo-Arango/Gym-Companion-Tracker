# We will store the standard routes for our website
from flask import Blueprint, render_template, request, flash, json, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Note

# We will define that this file is a blueprint of our app (contains routes (urls))
views = Blueprint("views", __name__)

# Whenever we're at the main part of our website, the function 'home' will run
@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route("/workout")
def workout():
    return render_template("workout.html", user=current_user)

@views.route("diet")
def diet():
    return render_template("diet.html", user=current_user)

@views.route("/log", methods=["GET", "POST"])
def log():
    if request.method == "POST": 
        note = request.form.get("note") # Gets the note from the HTML 

        if len(note) < 1:
            flash("Note is too short!", category="error") 
        else:
            # Providing the schema for the note
            new_note = Note(data=note, user_id=current_user.id)  
            # Adding the note to the database 
            db.session.add(new_note) 
            db.session.commit()
            flash("Note added!", category="success")
            return render_template("log.html", user=current_user)
        
    return render_template("log.html", user=current_user)

@views.route("/delete-note", methods=["POST"])
def delete_note():  
    # This function expects a JSON from the INDEX.js file 
    note = json.loads(request.data)
    noteId = note["noteId"]
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route("/challenge")
def challenge():
    return render_template("challenge.html", user=current_user)
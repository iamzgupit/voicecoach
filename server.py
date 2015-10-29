"""Voice Coach."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, AudioFile, Routine, AudioRoutine


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("home.html")

@app.route('/routine_builder')
def routine_builder():
    """Allows the user to build their routine of scales and instruction files."""

    return render_template("routine_builder.html")

@app.route('/routine_processor')
def process_routines():
    """Processes routine selected."""
    # pass
# #get data from checked boxes
# for each checked item:
# add it to audio-routines with that routine 

    return render_template("routine_selector.html")


@app.route('/routine_selector')
def select_routine():
    """Presents routines for users to select."""

    return "hooooooo"

@app.route('/play_routine')
def play_routine():
    """Plays the user's routine."""

    return "yodel"



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()




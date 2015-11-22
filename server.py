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

@app.route('/practice_selection')
def practice_selection():
    """Invites the user to choose either choose from saved routines or to create a new routine."""

    return render_template("practice_selection.html")

@app.route('/routine_builder')
def routine_builder():
    """Allows the user to build their routine of scales and instruction files."""

    return render_template("routine_builder.html")
                                           
@app.route('/routine_adder')
def add_routines():
    """add routine selected to routines table."""
 # add the routine name to the routines table 
    routine_name = request.args.get("RoutineName")
    new_routine = Routine(name=routine_name, u_id=1)

    db.session.add(new_routine)
    db.session.commit()

# #get data from checked boxes
    selected_audio_files = request.args.getlist("audio_file")
    for i in selected_audio_files:
        print "user selected audio file name: ", i
# # add the associated a_id to the audio_routines table 
        # by getting the associated a_id from the audio_files table
        audiofile = AudioFile.query.filter_by(name=i).first()
        print "audiofile from db: ", audiofile
        # add the routines id to the audio_routines table too
        new_audioroutine = AudioRoutine(r_id=new_routine.r_id, a_id=audiofile.a_id)
        db.session.add(new_audioroutine)
    db.session.commit()

    return redirect("/routine_displayer")
                                           
@app.route('/routine_displayer')
def display_routines():
    """get the stuff in that routine."""

    routines = Routine.query.all()
    return render_template("routine_selector.html",routines=routines)

@app.route('/routine_selector')
def select_routine():
    """Presents routines for users to select."""
    routines = Routine.query.order_by('r_id').all()

    return render_template("play_routine.html", routines=routines)

@app.route('/play_routine/<int:r_id>')
def play_routine(r_id):
    """Plays the user's routine."""
    # # query the audio_routines table using that r_id, get the a_id

    # routine = Routine.query.get(r_id) 
    # audiofiles = routine.audio_files
    
    audio_ids = AudioRoutine.query.filter_by(r_id=r_id).all()
    audio_stuff = []
    for row in audio_ids:
        audio_stuff.append(row.a_id)

    # get all the other stuff from the audio_files table using the a_id
    audiofiles=[]
    for i in audio_stuff:
        audiofiles.append(AudioFile.query.filter_by(a_id=i).one())

    return render_template("play_routine.html", audiofiles=audiofiles)

@app.route('/tuner')
def tuner():
    """Presents the tuner to the user."""

    return render_template("tuner.html")



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()
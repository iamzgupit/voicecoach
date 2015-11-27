from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AudioFile(db.Model):
    """Audio files (scales and instructions)."""

    __tablename__ = "audio_files"

    a_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    src = db.Column(db.String(64), nullable=True)
    name = db.Column(db.String(64), nullable=True)

    routines = db.relationship("Routine", secondary="audio_routines", backref="audio_files")

class Routine(db.Model):
    """Routines and their names."""

    __tablename__ = "routines"

    r_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=True)
    need = db.Column(db.String(64), nullable=True)
    u_id = db.Column(db.Integer, db.ForeignKey('users.u_id'))

    user = db.relationship('User', backref=db.backref("routines"))

class AudioRoutine(db.Model):
    """Combined audio files and routines"""

    __tablename__ = "audio_routines"

    ar_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    a_id = db.Column(db.Integer, db.ForeignKey('audio_files.a_id'))
    r_id = db.Column(db.Integer, db.ForeignKey('routines.r_id'))

class User(db.Model):
    """Holds user information"""

    __tablename__ = "users"

    u_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voicecoach.db'
#    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB.;"
    db.create_all()
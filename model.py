from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Audio_files(db.Model):
    """Audio files (scales and instructions)."""

    __tablename__ = "audio_files"

    a_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    src = db.Column(db.String(64), nullable=True)
    name = db.Column(db.String(64), nullable=True)

class Routines(db.Model):
    """Routines and their names."""

    __tablename__ = "routines"

    r_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=True)

class Audio_routines(db.Model):
    """Combined audio files and routines"""

    __tablename__ = "audio_routines"

    ar_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    a_id = db.Column(db.Integer, autoincrement=True)
    r_id = db.Column(db.Integer, autoincrement=True)
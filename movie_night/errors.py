from flask import render_template
from movie_night.extensions import db

def not_found_error(error):
    return render_template('404.html'), 404

def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
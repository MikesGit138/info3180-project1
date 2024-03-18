"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app import app
from flask import flash, render_template, request, redirect, url_for
from app.forms import PropertyForm
from app.models import Property
from werkzeug.utils import secure_filename
from . import db

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###
@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    form = PropertyForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join('UPLOAD_FOLDER', filename))

        property = Property(title=form.title.data, bedrooms=form.bedrooms.data, 
                            bathrooms=form.bathrooms.data, location=form.location.data, 
                            price=form.price.data, type=form.type.data, 
                            description=form.description.data, photo=filename)
        db.session.add(property)
        db.session.commit()
        
        flash('Property successfully added', 'success')
        return redirect(url_for('properties'))
    return render_template('create_property.html', form=form)

@app.route('/properties')
def properties():
    """Render the website's properties page."""
    return render_template('properties.html')

@app.route('/property/<propertyid>')
def property(propertyid):
    """Render the website's property page."""
    return render_template('property.html')

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

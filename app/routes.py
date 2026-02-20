from werkzeug.utils import secure_filename
import os
from flask import render_template, redirect, url_for, flash, request, current_app, send_from_directory
from app import app
from app import db
from app.models import Event
from app.forms import EventForm
from sqlalchemy.exc import IntegrityError


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/creating', methods=['GET', 'POST'])
def create_event():
    form = EventForm()

    if form.validate_on_submit():
        catering = ", ".join(service.replace("_"," ").capitalize() for service in form.catering.data) if form.catering.data else None

        file = form.attachment.data
        if file:  # Check if a file was uploaded
            filename = secure_filename(file.filename)  #Sanitise the filename to prevent security issues
            upload_folder = current_app.config['UPLOAD_FOLDER']  #Read the folder path for file uploads and store the result in `upload_folder`
            file.save(os.path.join(upload_folder, filename))
        else:
            filename = None

        event = Event(title=form.title.data, location=form.location.data, event_date=form.event_date.data, ticket_price=form.ticket_price.data, capacity=form.capacity.data, catering_ind=form.catering_ind.data, catering=catering, attachment_filename=filename)
        try:
            db.session.add(event)
            db.session.commit()
            flash(f"Event successfully added")
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash(f"Event has already been added")

    return render_template('create_event.html', form=form)

@app.route('/deleting/<int:event_id>')
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    flash(f"You have successfully deleted the event")
    return redirect(url_for('index'))

@app.route('/updating/<int:event_id>', methods=['GET','POST'])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    form = EventForm(obj=event) #This turns WTForms into an update form

    if form.validate_on_submit():
        event.ticket_price = form.ticket_price.data
        event.catering_ind = form.catering_ind.data

        catering = ", ".join(service.replace("_", " ").capitalize() for service in form.catering.data) if form.catering.data else None

        file = form.attachment.data
        if file:  # Check if a file was uploaded
            filename = secure_filename(file.filename)  # Sanitise the filename to prevent security issues
            upload_folder = current_app.config['UPLOAD_FOLDER']  # Read the folder path for file uploads and store the result in `upload_folder`
            file.save(os.path.join(upload_folder, filename))
        else:
            filename = None

        event.catering = catering
        event.attachment_filename = filename

        db.session.commit()
        flash(f"You have successfully updated the event")
        return redirect(url_for('index'))

    return render_template('updating.html', form=form)


@app.route('/searching', methods=['GET', 'POST'])
def search_event():
    query = Event.query  # Create the query object

    title = request.args.get("title")

    if title == 'music':
        query = query.filter(Event.title == "music")
    elif title == "comedy":
        query = query.filter(Event.title == "comedy")
    elif title == "theatre":
        query = query.filter(Event.title == "theatre")

    events = query.all()  # Actually making the query

    return render_template('searching.html', events=events, title=title)

@app.route('/downloading/<filename>')
def download_file(filename):
    upload_folder = current_app.config['UPLOAD_FOLDER'] #Read the folder path for file uploads and stores the result in `upload_folder`
    return send_from_directory(upload_folder,filename,as_attachment=True) #Returns the file specified by `filename` from the `upload_folder` directory for the client to download
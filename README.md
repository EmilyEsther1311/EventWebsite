# Event Management App

A modern, responsive web application built with Python and Flask that allows a user to seamlessly organise, track, and manage upcoming events. 

## Features

* **Create Events:** Log new events with details such as type (music, comedy, theatre), location, date, ticket price, capacity, and catering requirements.
* **File Uploads:** Upload supporting attachments images or PDFs) for each event.
* **View & Search:** View a comprehensive list of all logged events and filter them by event type.
* **Update & Delete:** Easily edit existing event details or completely remove events from the database.
* **Modern UI:** A clean, user-friendly interface powered by Bootstrap 5.

## Technologies Used

* **Backend:** Python 3, Flask
* **Database:** SQLite, Flask-SQLAlchemy (ORM)
* **Forms & Validation:** Flask-WTF, WTForms
* **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2 Templating

## Project Structure

```text
EventWebsite/
├── app/
│   ├── static/
│   │   └── css/
│   │       └── style.css       # Custom styling overrides
│   ├── templates/              # HTML Jinja2 templates (base, index, create, update, search)
│   ├── uploads/                # Directory where user-uploaded files are stored
│   ├── __init__.py             # App initialisation and configuration
│   ├── forms.py                # WTForms definitions for event handling
│   ├── models.py               # SQLAlchemy database models
│   └── routes.py               # Application URL routes and logic
├── .flaskenv                   # Environment variables for Flask
├── app.db                      # SQLite database file
├── config.py                   # Configuration settings
└── requirements.txt            # Python package dependencies
```

## Screenshots
<img width="1225" height="678" alt="Screenshot 2026-02-20 at 17 18 43" src="https://github.com/user-attachments/assets/bb2dfd75-c9ad-4158-9b4f-65ed26006ea5" />

<img width="1208" height="674" alt="Screenshot 2026-02-20 at 17 19 08" src="https://github.com/user-attachments/assets/18fed468-9270-41ea-952d-e8f6afc3893c" />

<img width="1223" height="679" alt="Screenshot 2026-02-20 at 17 19 19" src="https://github.com/user-attachments/assets/ea5439e8-666f-478a-b488-32d6de627e02" />

## Installation & Setup

Follow these steps to run the project locally on your machine.

### 1. Prerequisites
Ensure you have Python 3 installed on your system. 

### 2. Create a Virtual Environment (Optional but Recommended)
Navigate to the project directory in your terminal and create a virtual environment:
```bash
python -m venv venv

```

Activate the virtual environment:

* **Windows:** `venv\Scripts\activate`
* **macOS/Linux:** `source venv/bin/activate`

### 3. Install Dependencies

Install the required Python packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Initialise the Database

Before running the application for the first time, you need to set up the SQLite database. Run the following commands in your terminal:

```bash
flask shell
```

Once inside the interactive Python shell, run:

```python
from app import db
db.create_all()
exit()
```

### 5. Run the Application

Because the project uses a `.flaskenv` file, you can simply start the application with:

```bash
flask run
```

### 6. View the App

Open your web browser and navigate to:
`http://127.0.0.1:5000/`


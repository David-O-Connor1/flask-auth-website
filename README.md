# Flask Authentication Website

A web application built with Flask that implements user authentication using sessions and password hashing.

## Features

- User registration
- User login
- User logout
- Session management
- Protected dashboard page
- Password hashing
- Flash messages
- Form validation

## Technologies Used

- Python
- Flask
- Flask-WTF
- SQLite
- HTML
- CSS

## Project Structure

```
flask-auth-website
│
├── app.py
├── database.py
├── forms.py
├── schema.sql
├── requirements.txt
├── templates/
└── static/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/David-O-Connor1/flask-auth-website.git
```

Move into the project directory:

```bash
cd flask-auth-website
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

## Concepts Demonstrated

- Flask routing
- Template inheritance
- Sessions
- Decorators
- Password hashing
- SQLite databases
- Form validation
- Authentication and authorization
- Git and GitHub workflow

## Future Improvements

- Improved styling
- User profile page
- Change password functionality
- Email verification
- Remember me functionality
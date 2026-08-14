# Arun C S — Developer Portfolio

A modern, dark-first personal portfolio website built with Django, Bootstrap 5, and vanilla JavaScript.

## Features

- Responsive dark/light theme with localStorage persistence
- Animated hero terminal
- Interactive CLI terminal (type `help` to start)
- Filterable project cards with detail modals
- Animated vertical timeline
- Functional contact form — saves to Django database
- Contact messages viewable in Django Admin
- Scroll reveal animations
- Custom cursor (desktop)
- SEO meta tags

## Tech Stack

- **Backend:** Python 3, Django 4
- **Frontend:** Bootstrap 5, Vanilla JS, CSS custom properties
- **Database:** SQLite (dev) — swap to PostgreSQL for production
- **Icons:** Bootstrap Icons, Devicons

## Folder Structure

```
portfolio/          Django project settings
main/               App — models, views, forms, admin
templates/          base.html, home.html
static/
  css/style.css     All styles
  js/script.js      All JS
  images/           Project images / placeholders
  resume/           Put Arun-CS-Resume.pdf here
db.sqlite3          SQLite database
```

## Installation

```bash
pip install django pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit: http://127.0.0.1:8000

## Development Commands

```bash
python manage.py runserver          # start dev server
python manage.py makemigrations     # after model changes
python manage.py migrate            # apply migrations
python manage.py createsuperuser    # create admin user
python manage.py collectstatic      # for production
```

## How To: Add a Project

Open `main/views.py` and add an entry to the `PROJECTS` list:

```python
{
    'id': 5,
    'title': 'My New Project',
    'category': 'backend',           # backend | fullstack | aiml | frontend
    'category_label': 'Backend',
    'description': 'Short description shown on the card.',
    'long_description': 'Longer description shown in the modal.',
    'technologies': ['Python', 'Django'],
    'features': ['Feature one', 'Feature two'],
    'github': 'https://github.com/arun-c-s-07/project',
    'live': '',                      # leave empty if no live demo
    'image': 'images/project-placeholder.svg',
},
```

## How To: Update Profile Info

Open `portfolio/settings.py` and edit the `PORTFOLIO_CONFIG` dict:

```python
PORTFOLIO_CONFIG = {
    'name': 'Arun C S',
    'email': 'your.email@example.com',
    'github': 'https://github.com/arun-c-s-07',
    'linkedin': 'https://linkedin.com/in/your-profile',
    'leetcode': 'https://leetcode.com/your-profile',
    'resume_path': 'resume/Arun-CS-Resume.pdf',
}
```

## How To: Replace Resume

Drop your PDF at:

```
static/resume/Arun-CS-Resume.pdf
```

The download button appears automatically once the file exists.

## How To: Update Skills / Timeline

Open `main/views.py`:
- Edit the `SKILLS` dict for skill cards
- Edit the `TIMELINE` list for the journey section
- Edit `AIML_AREAS` for the AI/ML section
- Edit `CURRENTLY_LEARNING` for the learning tags

## How To: View Contact Messages

1. Go to http://127.0.0.1:8000/admin
2. Log in with your superuser credentials
3. Click **Contact Messages**

Default admin credentials (change immediately):
- Username: `admin`
- Password: `admin123`

## Production Deployment Checklist

- Set `DEBUG = False` in settings
- Set a strong `SECRET_KEY`
- Add your domain to `ALLOWED_HOSTS`
- Run `python manage.py collectstatic`
- Use PostgreSQL instead of SQLite
- Serve static files via Nginx / WhiteNoise

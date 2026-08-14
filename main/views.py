from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .models import Project, Skill, TimelineEntry, AIMLArea, LearningItem, Certification, Achievement, Resume

# ── Fallback data (used only if DB tables are empty) ─────────────────────────

FALLBACK_PROJECTS = [
    {
        'id': 1,
        'title': 'Sponsorship / Offers Platform',
        'category': 'fullstack',
        'category_label': 'Full Stack',
        'description': 'A web platform for managing sponsorship/offers and applications with a Django backend and modern React frontend.',
        'long_description': 'Built a full-stack web platform that enables organisations to post sponsorship opportunities and allows users to apply and manage submissions. Features a Django REST Framework backend with JWT authentication and a React + Vite frontend.',
        'technologies': ['Django', 'Django REST Framework', 'React', 'Vite', 'PostgreSQL'],
        'features': [
            'User authentication and authorisation',
            'Sponsorship listing and application management',
            'Django REST Framework API backend',
            'React frontend with Vite build tooling',
            'Admin dashboard for managing listings',
        ],
        'github': 'https://github.com/arun-c-s-07',
        'live': '',
        'image_url': None,
    },
    {
        'id': 2,
        'title': 'Contact Management API',
        'category': 'backend',
        'category_label': 'Backend',
        'description': 'A REST API for handling contact form submissions with Django REST Framework and React frontend integration.',
        'long_description': 'Developed a robust REST API using Django REST Framework to handle contact form data. Includes validation, serialisation, and a React frontend for seamless form submissions.',
        'technologies': ['Django', 'Django REST Framework', 'React'],
        'features': [
            'RESTful API endpoints',
            'Form validation and serialisation',
            'React frontend integration',
            'Admin panel for message management',
        ],
        'github': 'https://github.com/arun-c-s-07',
        'live': '',
        'image_url': None,
    },
    {
        'id': 3,
        'title': 'AI Profession Image Generator',
        'category': 'aiml',
        'category_label': 'AI / ML',
        'description': 'An experimental AI-powered application that transforms uploaded images into profession-themed generated images using AI APIs.',
        'long_description': 'An experimental project exploring AI image generation. Users upload a photo and select a profession; the application calls an AI API to generate a profession-themed version of the image.',
        'technologies': ['Python', 'Django', 'React', 'AI API'],
        'features': [
            'Image upload and processing',
            'AI API integration for image generation',
            'Profession theme selection',
            'Django backend serving React frontend',
        ],
        'github': 'https://github.com/arun-c-s-07',
        'live': '',
        'image_url': None,
    },
    {
        'id': 4,
        'title': 'Skill Swap Hub',
        'category': 'frontend',
        'category_label': 'Frontend',
        'description': 'A platform concept for users to discover and exchange skills, built with HTML, CSS and JavaScript.',
        'long_description': 'A frontend concept project exploring a platform where users can list skills they offer and skills they want to learn.',
        'technologies': ['HTML', 'CSS', 'JavaScript'],
        'features': [
            'Skill listing and discovery interface',
            'Clean and responsive UI',
            'JavaScript-powered filtering',
            'Mobile-friendly layout',
        ],
        'github': 'https://github.com/arun-c-s-07',
        'live': '',
        'image_url': None,
    },
]

FALLBACK_SKILLS = {
    'Programming': [
        {'name': 'Python',     'icon': 'devicon-python-plain',     'color': '#3776AB'},
        {'name': 'JavaScript', 'icon': 'devicon-javascript-plain', 'color': '#F7DF1E'},
        {'name': 'C',          'icon': 'devicon-c-plain',          'color': '#A8B9CC'},
    ],
    'Backend': [
        {'name': 'Django',                'icon': 'devicon-django-plain',    'color': '#092E20'},
        {'name': 'Django REST Framework', 'icon': 'devicon-django-plain',    'color': '#092E20'},
        {'name': 'REST APIs',             'icon': 'bi bi-diagram-3',         'color': '#FF6B35'},
    ],
    'Frontend': [
        {'name': 'HTML',       'icon': 'devicon-html5-plain',       'color': '#E34F26'},
        {'name': 'CSS',        'icon': 'devicon-css3-plain',        'color': '#1572B6'},
        {'name': 'Bootstrap',  'icon': 'devicon-bootstrap-plain',   'color': '#7952B3'},
        {'name': 'JavaScript', 'icon': 'devicon-javascript-plain',  'color': '#F7DF1E'},
        {'name': 'React',      'icon': 'devicon-react-original',    'color': '#61DAFB'},
    ],
    'Database': [
        {'name': 'MySQL',      'icon': 'devicon-mysql-plain',       'color': '#4479A1'},
        {'name': 'SQLite',     'icon': 'devicon-sqlite-plain',      'color': '#003B57'},
        {'name': 'PostgreSQL', 'icon': 'devicon-postgresql-plain',  'color': '#336791'},
    ],
    'Tools': [
        {'name': 'Git',    'icon': 'devicon-git-plain',      'color': '#F05032'},
        {'name': 'GitHub', 'icon': 'devicon-github-original','color': '#181717'},
        {'name': 'VS Code','icon': 'devicon-vscode-plain',   'color': '#007ACC'},
    ],
    'AI / ML': [
        {'name': 'NumPy',           'icon': 'devicon-numpy-original',  'color': '#013243'},
        {'name': 'Pandas',          'icon': 'devicon-pandas-original', 'color': '#150458'},
        {'name': 'Matplotlib',      'icon': 'bi bi-graph-up',          'color': '#11557C'},
        {'name': 'Machine Learning','icon': 'bi bi-cpu',               'color': '#FF6B6B'},
        {'name': 'Deep Learning',   'icon': 'bi bi-layers',            'color': '#4ECDC4'},
        {'name': 'Computer Vision', 'icon': 'bi bi-eye',               'color': '#45B7D1'},
        {'name': 'Generative AI',   'icon': 'bi bi-stars',             'color': '#96CEB4'},
    ],
}

FALLBACK_TIMELINE = [
    {'year': '2023',      'title': 'Started B.Tech CSE',                  'description': 'Began my Computer Science and Engineering degree.', 'is_current': False},
    {'year': '2024',      'title': 'Python & DSA',                        'description': 'Started learning Python seriously and practising Data Structures and Algorithms.', 'is_current': False},
    {'year': '2025',      'title': 'Django & Backend Development',        'description': 'Started building backend applications with Django and Django REST Framework.', 'is_current': False},
    {'year': '2025–2026', 'title': 'REST APIs & Full-Stack Projects',     'description': 'Built multiple REST API projects and full-stack applications.', 'is_current': False},
    {'year': '2026',      'title': 'Exploring React & AI/ML',             'description': 'Expanding into modern React development and AI/ML.', 'is_current': False},
    {'year': 'Current',   'title': 'Building & Preparing',                'description': 'Actively building projects and preparing for software development opportunities.', 'is_current': True},
]

FALLBACK_AIML = [
    {'title': 'Machine Learning',          'icon': 'bi bi-cpu',       'description': 'Exploring supervised and unsupervised learning, model training and evaluation.'},
    {'title': 'Deep Learning',             'icon': 'bi bi-layers',    'description': 'Learning neural network architectures and experimenting with deep learning concepts.'},
    {'title': 'Computer Vision',           'icon': 'bi bi-eye',       'description': 'Exploring image processing and computer vision applications.'},
    {'title': 'Natural Language Processing','icon': 'bi bi-chat-text','description': 'Learning text processing, NLP fundamentals and how language models work.'},
    {'title': 'Generative AI',             'icon': 'bi bi-stars',     'description': 'Experimenting with generative AI APIs and building AI-powered features.'},
]

FALLBACK_LEARNING = [
    {'name': 'Advanced Django',        'icon': 'devicon-django-plain'},
    {'name': 'Django REST Framework',  'icon': 'devicon-django-plain'},
    {'name': 'React',                  'icon': 'devicon-react-original'},
    {'name': 'PostgreSQL',             'icon': 'devicon-postgresql-plain'},
    {'name': 'Docker',                 'icon': 'devicon-docker-plain'},
    {'name': 'Cloud / AWS',            'icon': 'bi bi-cloud'},
    {'name': 'Machine Learning',       'icon': 'bi bi-cpu'},
    {'name': 'Computer Vision',        'icon': 'bi bi-eye'},
    {'name': 'Generative AI',          'icon': 'bi bi-stars'},
]

PLACEHOLDER_IMAGE = 'images/project-placeholder.svg'


# ── Helpers ───────────────────────────────────────────────────────────────────

def _get_projects():
    qs = Project.objects.filter(is_featured=True)
    if not qs.exists():
        return FALLBACK_PROJECTS

    result = []
    for p in qs:
        result.append({
            'id':             p.id,
            'title':          p.title,
            'category':       p.category,
            'category_label': p.get_category_label(),
            'description':    p.description,
            'long_description': p.long_description,
            'technologies':   p.get_technologies_list(),
            'features':       p.get_features_list(),
            'github':         p.github,
            'live':           p.live,
            'image_url':      p.get_image_url(),
        })
    return result


def _get_skills():
    qs = Skill.objects.all()
    if not qs.exists():
        return FALLBACK_SKILLS

    skills = {}
    for skill in qs:
        skills.setdefault(skill.category, []).append({
            'name':  skill.name,
            'icon':  skill.icon,
            'color': skill.color,
        })
    return skills


def _get_timeline():
    qs = TimelineEntry.objects.all()
    if not qs.exists():
        return FALLBACK_TIMELINE
    return list(qs.values('year', 'title', 'description', 'is_current'))


def _get_aiml():
    qs = AIMLArea.objects.all()
    if not qs.exists():
        return FALLBACK_AIML
    return list(qs.values('title', 'icon', 'description'))


def _get_learning():
    qs = LearningItem.objects.all()
    if not qs.exists():
        return FALLBACK_LEARNING
    return list(qs.values('name', 'icon'))


def _get_certifications():
    return list(Certification.objects.all().values('title', 'issuer', 'date', 'credential_url'))


def _get_achievements():
    return list(Achievement.objects.all().values('title', 'description', 'date'))


def _get_resume_url():
    resume = Resume.objects.filter(is_active=True).first()
    if resume:
        return resume.file.url
    return None


# ── View ──────────────────────────────────────────────────────────────────────

def home(request):
    config = settings.PORTFOLIO_CONFIG
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! Your message has been received.")
            return redirect('home')
        else:
            messages.error(request, "Please fix the errors below and try again.")

    context = {
        'config':             config,
        'projects':           _get_projects(),
        'skills':             _get_skills(),
        'timeline':           _get_timeline(),
        'aiml_areas':         _get_aiml(),
        'currently_learning': _get_learning(),
        'certifications':     _get_certifications(),
        'achievements':       _get_achievements(),
        'resume_url':         _get_resume_url(),
        'contact_form':       form,
        'placeholder_image':  PLACEHOLDER_IMAGE,
    }
    return render(request, 'home.html', context)

import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Ensure media directories exist at runtime
BASE_DIR = Path(__file__).resolve().parent.parent
(BASE_DIR / 'media' / 'resume').mkdir(parents=True, exist_ok=True)
(BASE_DIR / 'media' / 'projects').mkdir(parents=True, exist_ok=True)

application = get_wsgi_application()

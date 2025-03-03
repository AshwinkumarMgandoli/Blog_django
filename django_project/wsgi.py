# wsgi.py in your_project/
import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'application' object
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

# The WSGI application object
application = get_wsgi_application()

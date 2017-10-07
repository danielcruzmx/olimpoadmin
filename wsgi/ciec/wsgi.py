"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

# GETTING-STARTED: change 'admincon' to your project name:
#os.environ["DJANGO_SETTINGS_MODULE"] = "ciec.settings"

sys.path.append('/Users/danielcruzmx/olimpo/administra/wsgi/ciec/admincon')
sys.path.append('/Users/danielcruzmx/olimpo/administra/wsgi/ciec')

os.environ["DJANGO_SETTINGS_MODULE"] = "admincon.settings"

application = get_wsgi_application()

"""
WSGI config for edisposisi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edisposisi.settings')

application = get_wsgi_application()

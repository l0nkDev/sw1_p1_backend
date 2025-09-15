"""
ASGI config for sw1_p1_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sw1_p1_backend.settings')
from sw1_p1_backend import routing

application = routing.application

"""
ASGI config for sw1_p1_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sw1_p1_backend.settings')
django.setup()
# This import is intentionally placed here due to Django Channels' app loading
# requirements, as it relies on the app registry being ready.
from sw1_p1_backend import routing  # noqa: E402

application = routing.application

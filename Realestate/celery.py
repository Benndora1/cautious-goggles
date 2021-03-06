from __future__ import absolute_import

import os

from celery import Celery
from Realestate.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Realestate.settings.development")

app = Celery("Realestate")

app.config_from_object("Realestate.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)

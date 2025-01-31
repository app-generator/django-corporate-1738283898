# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

#__CELERY__
from .celery import app as celery_app

__all__ = ('celery_app',)



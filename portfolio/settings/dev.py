import os
from os import path
from pathlib import Path

from .base import BASE_DIR

DEBUG = True

# LOCAL STATIC + MEDIA FILES
STATIC_URL = 'static/'
# STATIC_ROOT = path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = [
   str(BASE_DIR.joinpath('static'))
]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

print('in dev using local static prod db and prod media')
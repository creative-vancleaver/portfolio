import os
from os import path
from pathlib import Path

from .base import BASE_DIR

from decouple import config

# DEBUG === FALSE FOR PRODUCTION
DEBUG = False

# SERVE STATIC FILES WITH AWS S3 VIA CLOUD FRONT

# AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

# AWS_STORAGE_BUCKET_NAME = 'jvc-design'
# AWS_S3_CUSTOM_DOMAIN = 'd1q6g24kllzypv.cloudfront.net'

AWS_LOCATION = 'static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = 'https://%s/%s/' % (config("S3_CUSTOM_DOMAIN"), AWS_LOCATION)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# DEFAULT_FILE_STORAGE = 'portfolio.storage_backends.MediaStorage'

# STATICFILES_IGNORE_PATTERnS = [
#     'CVS', 
#     '.*',
#     '*~',
#     '../static/js/__tests__/*',
#     'test.*.js',
# ]

print('in prod using prod db prod media and prod static')
from decouple import config
from .base import *

if (config("DEV_ENV") == 'True'):
    
    # USE LOCAL STATIC + LOCAL MEDIA WITH AWS RDS DB
    
    from .dev import *
    
else:
    
    # SERVE STATIC + MEDIA FROM AWS S3 WITH AWS RDS DB
    
    from .prod import *
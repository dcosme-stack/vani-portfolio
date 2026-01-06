from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

STATICFILES_DIRS += [
    BASE_DIR / "static_dev", 
]
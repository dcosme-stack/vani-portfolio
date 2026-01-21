from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost","unlocative-unremorsefully-fredericka.ngrok-free.dev", ".ngrok.io", ".ngrok-free.app",]

STATICFILES_DIRS += [
    BASE_DIR / "static_dev", 
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


CSRF_TRUSTED_ORIGINS = [
    "https://*.ngrok.io",
    "https://*.ngrok-free.app",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-938l$hw9k8_c)bibmjvsufs!*fv+omt9(jos832$cr4$7#hjob'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'USER': 'root',
        'PASSWORD': '555429ea',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
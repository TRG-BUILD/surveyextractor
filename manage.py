import sys
import django
from django.conf import settings

from pathlib import Path


BASE_DIR = './' #Path(__file__).resolve()

INSTALLED_APPS = [
    'orm',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.sqlite3',
    }
,
}



settings.configure(
    INSTALLED_APPS = INSTALLED_APPS,
    DATABASES = DATABASES,
)

django.setup()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

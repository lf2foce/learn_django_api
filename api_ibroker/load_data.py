from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand
from .models import Article

DATETIME_FORMET = '%d/%m/%Y %H:%M'
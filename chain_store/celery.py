import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chain_store.settings')
app = Celery('chain_store')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'increase_company_dept_every_3_hours': {
        'task': 'applications.companies.tasks.increase_company_debt',
        'schedule': crontab(minute=0, hour='*/3'),
    },
    'reduce_company_dept_every_day_at_6:30': {
        'task': 'applications.companies.tasks.reduce_company_debt',
        'schedule': crontab(hour=6, minute=30),
    },
}

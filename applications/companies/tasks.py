from django.core.mail import EmailMultiAlternatives

from applications.companies.services import increase_debt, reduce_debt
from chain_store.celery import app


@app.task
def async_cancel_debt(queryset):
    queryset.update(debt=0)


@app.task
def increase_company_debt():
    increase_debt.delay()


@app.task
def reduce_company_debt():
    reduce_debt.delay()


@app.task
def send_by_email(user_email, image_path):
    msg = EmailMultiAlternatives(
        subject='QRcode with company email',
        body='Scan QRcode and get company email',
        from_email='app@mailhog.com',
        to=(f'{user_email}',),
    )
    msg.attach_file(image_path)
    msg.send()

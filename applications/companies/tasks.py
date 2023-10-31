import tempfile

import qrcode
from django.core.mail import EmailMultiAlternatives

from applications.companies import services
from applications.companies.models import Company
from chain_store.celery import app


@app.task
def cancel_companies_debt(ids):
    Company.objects.filter(pk__in=ids).update(debt=0)


@app.task
def increase_companies_debt():
    return services.increase_debt()


@app.task
def reduce_companies_debt():
    return services.reduce_debt()


@app.task
def send_qrcode_email(company_email, user_email):
    msg = EmailMultiAlternatives(
        subject='QRcode with company email',
        body='Scan QRcode and get company email',
        from_email='app@mailhog.com',
        to=(f'{user_email}',),
    )

    with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
        img = qrcode.make(company_email)
        img.save(tmp.name)
        tmp.seek(0)
        msg.attach("qrcode.png", tmp.read(), "image/png")

    msg.send()

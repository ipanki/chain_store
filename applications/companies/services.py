import random

import qrcode

from applications.companies.models import Company
from chain_store.celery import app


@app.task
def increase_debt():
    companies = Company.objects.all()
    for company in companies:
        if company.category == 'factory':
            continue
        company.debt += random.randint(5, 500)
        company.save()


@app.task
def reduce_debt():
    companies = Company.objects.all()
    for company in companies:
        if company.category == 'factory':
            continue
        part_debt = random.randint(100, 10000)
        if company.debt >= part_debt:
            company.debt -= part_debt
        else:
            company.debt = 0
        company.save()


def generate_qrcode(email):
    img = qrcode.make(email)
    filename = f"qrcode-{email}-{random.randint(1,99999)}.png"
    img.save(filename)
    return filename

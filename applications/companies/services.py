import random

from applications.companies.models import Company


def increase_debt():
    companies = Company.objects.all()
    for company in companies:
        if company.category == 'factory':
            continue
        company.debt += random.randint(5, 500)
        company.save()


def reduce_debt():
    companies = Company.objects.exclude(category="factory")
    for company in companies:
        part_debt = random.randint(100, 10000)
        if company.debt >= part_debt:
            company.debt -= part_debt
        else:
            company.debt = 0
        company.save()

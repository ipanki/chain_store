# Generated by Django 3.2.22 on 2023-10-25 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factory', '0001_initial'),
        ('contacts', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('debt', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('contacts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dealerships_contacts', to='contacts.contacts')),
                ('employees', models.ManyToManyField(blank=True, null=True, related_name='dealerships_employees', to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dealerships_contacts', to='factory.factory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealerships', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DealershipProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('count', models.PositiveIntegerField(default=1)),
                ('dealership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dealerships', to='dealership.dealership')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dealerships_products', to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
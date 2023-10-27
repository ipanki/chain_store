# Generated by Django 3.2.22 on 2023-10-27 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=50)),
                ('launch_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

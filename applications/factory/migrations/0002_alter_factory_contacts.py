# Generated by Django 3.2.22 on 2023-10-25 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
        ('factory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='contacts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='factories_contacts', to='contacts.contacts'),
        ),
    ]

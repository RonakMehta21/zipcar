# Generated by Django 2.2.12 on 2020-05-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='last_membership_date',
            field=models.DateField(default=None),
        ),
    ]
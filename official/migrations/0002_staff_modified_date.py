# Generated by Django 3.1.3 on 2020-11-14 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

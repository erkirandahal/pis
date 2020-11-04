# Generated by Django 3.1.3 on 2020-11-03 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('officedata', '0002_auto_20201102_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officename_nepali', models.CharField(max_length=100)),
                ('officename_english', models.CharField(max_length=100)),
                ('officeaddress', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('officetype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='officedata.officetype')),
            ],
        ),
    ]
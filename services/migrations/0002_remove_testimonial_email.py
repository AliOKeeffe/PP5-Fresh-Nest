# Generated by Django 3.2 on 2022-09-26 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='email',
        ),
    ]

# Generated by Django 3.2 on 2022-10-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='enquiry_type',
            field=models.CharField(choices=[('DS', 'Design Consultation Enquiry'), ('PQ', 'Product Query'), ('OQ', 'Order Query'), ('O', 'Other')], default='DS', max_length=254),
        ),
    ]

# Generated by Django 3.0.3 on 2020-05-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbeauty', '0002_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]

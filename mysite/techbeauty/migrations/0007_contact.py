# Generated by Django 3.0.3 on 2020-05-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbeauty', '0006_auto_20200509_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('txt', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
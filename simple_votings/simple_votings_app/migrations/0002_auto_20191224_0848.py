# Generated by Django 3.0.1 on 2019-12-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_votings_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='end_time',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]

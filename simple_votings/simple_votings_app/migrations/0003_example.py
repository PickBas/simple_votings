# Generated by Django 3.0.1 on 2019-12-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_votings_app', '0002_auto_20191224_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=200)),
                ('galochka', models.BooleanField()),
            ],
        ),
    ]

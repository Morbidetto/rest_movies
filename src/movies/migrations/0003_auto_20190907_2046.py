# Generated by Django 2.2.5 on 2019-09-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190907_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='metascore',
            field=models.CharField(max_length=25),
        ),
    ]

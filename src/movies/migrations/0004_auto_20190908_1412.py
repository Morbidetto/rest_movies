# Generated by Django 2.2.5 on 2019-09-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20190907_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-23 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_somemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SomeModel',
        ),
    ]
# Generated by Django 3.2 on 2021-04-24 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clicker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='click',
            options={'ordering': ['-timestamp']},
        ),
    ]

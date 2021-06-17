# Generated by Django 3.2.4 on 2021-06-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=120)),
                ('email', models.EmailField(blank=True, max_length=120)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('building_name', models.CharField(blank=True, max_length=100)),
                ('street_name', models.CharField(blank=True, max_length=100)),
                ('locality', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('postcode', models.CharField(blank=True, max_length=8)),
                ('flag', models.CharField(choices=[('example', 'example'), ('Electoral', 'Electoral'), ('Existing Clients', 'Existing Clients'), ('Lapsed', 'Lapsed'), ('test', 'test'), ('WebOffer', 'WebOffer')], default='example', max_length=100)),
            ],
            options={
                'ordering': ['company_name'],
            },
        ),
    ]

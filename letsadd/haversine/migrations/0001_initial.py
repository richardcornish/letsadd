# Generated by Django 3.2.3 on 2021-06-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('slug', models.SlugField(unique=True)),
                ('location', models.CharField(max_length=254)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('established', models.DateField()),
                ('area', models.FloatField(help_text='acres')),
                ('visitors', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('whs', models.BooleanField(default=False, verbose_name='World Heritage Site')),
                ('br', models.BooleanField(default=False, verbose_name='Biosphere Reserve')),
                ('url', models.URLField(verbose_name='URL')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-15 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agents.agent')),
            ],
        ),
    ]
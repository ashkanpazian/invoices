# Generated by Django 5.0.4 on 2024-04-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.IntegerField(),
        ),
    ]
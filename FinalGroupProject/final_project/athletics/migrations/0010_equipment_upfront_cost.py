# Generated by Django 5.0.1 on 2024-04-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletics', '0009_income_date_recorded'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='upfront_cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

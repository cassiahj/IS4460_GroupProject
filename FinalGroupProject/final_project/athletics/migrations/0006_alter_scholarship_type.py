# Generated by Django 5.0.1 on 2024-04-09 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletics', '0005_rename_date_scholarship_date_awarded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='type',
            field=models.CharField(choices=[('AC', 'Academic'), ('GR', 'Grant'), ('ATH', 'Athletic'), ('ME', 'Merit'), ('FI', 'Financial Need'), ('OT', 'Other')], max_length=3),
        ),
    ]

# Generated by Django 5.0.1 on 2024-04-09 02:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletics', '0003_remove_scholarship_id_remove_scholarship_team_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='athlete',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='athletics.athlete'),
        ),
    ]
# Generated by Django 5.0.1 on 2024-04-09 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletics', '0007_remove_income_id_remove_income_team_id_income_team_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='big event', max_length=50),
            preserve_default=False,
        ),
    ]

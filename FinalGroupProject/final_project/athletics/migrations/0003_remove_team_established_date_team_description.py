# Generated by Django 5.0.1 on 2024-03-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletics', '0002_remove_team_id_alter_team_team_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='established_date',
        ),
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
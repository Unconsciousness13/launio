# Generated by Django 4.0.3 on 2022-03-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_remove_team_trainers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesindividual',
            name='competition_place_on_board',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='notesteam',
            name='competition_place_on_board',
            field=models.IntegerField(unique=True),
        ),
    ]
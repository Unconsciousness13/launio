# Generated by Django 4.0.3 on 2022-03-25 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_remove_notesindividual_competition_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notesindividual',
            name='competition',
        ),
        migrations.AddField(
            model_name='notesindividual',
            name='competition',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='club.competition'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-04 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_alter_notesindividual_competition_place_on_board_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='email_address',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]

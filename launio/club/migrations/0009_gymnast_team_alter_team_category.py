# Generated by Django 4.0.3 on 2022-03-25 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_alter_notesindividual_competition_place_on_board_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymnast',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='club.team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='category',
            field=models.CharField(choices=[('Sin COnjunto', 'Sin Conjunto'), ('Pre-benjamín', 'Pre-benjamín'), ('Benjamín', 'Benjamín'), ('Alevín', 'Alevín'), ('Infantil', 'Infantil'), ('Cadete', 'Cadete')], max_length=30),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-04 08:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_alter_notesindividual_nota_competition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='competition_club_organisation',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='gymnast',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='notesindividual',
            name='competition_place_on_board',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='notesindividual',
            name='nota_competition',
            field=models.DecimalField(decimal_places=3, max_digits=5, validators=[django.core.validators.MinValueValidator(0.001)]),
        ),
        migrations.AlterField(
            model_name='notesteam',
            name='competition_place_on_board',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='notesteam',
            name='nota_competition',
            field=models.DecimalField(decimal_places=3, max_digits=5, validators=[django.core.validators.MinValueValidator(0.001)]),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]

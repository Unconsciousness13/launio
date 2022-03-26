# Generated by Django 4.0.3 on 2022-03-26 17:02

from django.db import migrations, models
import validators.image_validator


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0011_remove_team_category_gymnast_team_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='gymnasts/', validators=[validators.image_validator.MaxFileSizeInMbValidator(2)]),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
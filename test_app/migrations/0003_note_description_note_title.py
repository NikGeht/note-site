# Generated by Django 4.2.5 on 2023-09-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_note_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

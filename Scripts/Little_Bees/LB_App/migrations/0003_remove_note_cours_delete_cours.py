# Generated by Django 4.2.3 on 2023-07-24 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LB_App', '0002_remove_note_note_note_chant_note_dessin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='cours',
        ),
        migrations.DeleteModel(
            name='Cours',
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-08 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colaborador',
            old_name='location',
            new_name='Localidad',
        ),
    ]

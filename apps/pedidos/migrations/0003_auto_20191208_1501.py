# Generated by Django 2.2.7 on 2019-12-08 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20191208_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colaborador',
            options={'ordering': ['edad'], 'verbose_name': 'Colaborador', 'verbose_name_plural': 'Colaborador'},
        ),
        migrations.RenameField(
            model_name='colaborador',
            old_name='age',
            new_name='edad',
        ),
    ]
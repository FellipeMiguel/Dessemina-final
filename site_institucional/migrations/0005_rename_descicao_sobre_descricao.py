# Generated by Django 4.0.6 on 2022-07-17 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_institucional', '0004_footer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sobre',
            old_name='descicao',
            new_name='descricao',
        ),
    ]
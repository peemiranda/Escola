# Generated by Django 4.0.4 on 2022-10-24 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='data_de_nascimento',
            new_name='data_nascimento',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='cogigo_curso',
            new_name='codigo_curso',
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-11 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejercicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='comentario',
            field=models.CharField(default='Cuentanos que te parece la experiencia del usuario', max_length=200),
        ),
    ]

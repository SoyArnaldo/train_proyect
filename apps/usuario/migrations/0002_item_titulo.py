# Generated by Django 4.2.6 on 2023-10-08 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='titulo',
            field=models.CharField(default='Zona del cuerpo a entrenar', max_length=120),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_customuser_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='comentarios',
            field=models.TextField(blank=True),
        ),
    ]
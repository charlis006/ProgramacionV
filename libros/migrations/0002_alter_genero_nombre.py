# Generated by Django 5.2.1 on 2025-07-09 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

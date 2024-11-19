# Generated by Django 5.1 on 2024-11-19 04:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0003_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(default='example@example.com', max_length=100, unique=True, validators=[django.core.validators.EmailValidator(message='Ingrese un correo electrónico válido.')]),
        ),
    ]
# Generated by Django 3.2.13 on 2022-09-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0005_auto_20220930_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='cpf',
            field=models.CharField(max_length=14, verbose_name='CPF do candidato'),
        ),
    ]
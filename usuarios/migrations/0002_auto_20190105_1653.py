# Generated by Django 2.1.5 on 2019-01-05 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]

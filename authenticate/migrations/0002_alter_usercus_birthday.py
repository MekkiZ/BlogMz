# Generated by Django 4.1.7 on 2023-06-03 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercus',
            name='birthday',
            field=models.DateField(default='01/01/1111'),
        ),
    ]

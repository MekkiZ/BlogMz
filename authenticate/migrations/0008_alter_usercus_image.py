# Generated by Django 4.1.7 on 2023-06-30 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0007_remove_usercus_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Profile/%Y/%m/%d'),
        ),
    ]
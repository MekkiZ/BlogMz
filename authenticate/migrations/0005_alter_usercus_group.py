# Generated by Django 4.1.7 on 2023-06-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_alter_usercus_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercus',
            name='group',
            field=models.CharField(blank=True, choices=[('regular', 'regular'), ('moderator', 'moderator'), ('publisher', 'publisher')], default='regular', max_length=30),
        ),
    ]

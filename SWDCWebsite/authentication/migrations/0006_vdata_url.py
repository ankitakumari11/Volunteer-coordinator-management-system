# Generated by Django 4.1.2 on 2022-11-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_vdata_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='vdata',
            name='url',
            field=models.URLField(default=''),
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-12 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_vdata_cordinator'),
    ]

    operations = [
        migrations.AddField(
            model_name='vdata',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]

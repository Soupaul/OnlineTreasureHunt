# Generated by Django 2.1.4 on 2020-02-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0006_auto_20200205_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='countdown',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-22 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chimp',
            name='weight',
            field=models.IntegerField(default=150),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.6 on 2020-01-01 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_chimp_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('shiftSeg', models.CharField(choices=[('1', '1st shift'), ('2', '2nd shift'), ('3', '3rd shift')], default='1', max_length=1)),
                ('chimp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Chimp')),
            ],
        ),
    ]

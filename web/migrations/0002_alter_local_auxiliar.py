# Generated by Django 3.2.3 on 2021-05-23 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='auxiliar',
            field=models.IntegerField(choices=[(0, 'O'), (1, 'A')], max_length=1),
        ),
    ]

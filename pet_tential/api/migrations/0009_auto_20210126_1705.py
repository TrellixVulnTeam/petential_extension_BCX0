# Generated by Django 3.1.5 on 2021-01-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_walk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walk',
            name='duration',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='walk',
            name='time',
            field=models.TimeField(),
        ),
    ]

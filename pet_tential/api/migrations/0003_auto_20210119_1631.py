# Generated by Django 3.1.5 on 2021-01-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_food_treats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='treats',
            field=models.IntegerField(default=0),
        ),
    ]
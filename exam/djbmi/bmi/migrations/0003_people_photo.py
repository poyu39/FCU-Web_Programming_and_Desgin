# Generated by Django 4.2.1 on 2023-05-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmi', '0002_alter_people_tall_alter_people_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
# Generated by Django 5.1.4 on 2024-12-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('army', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trooptype',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание этого войска'),
        ),
    ]

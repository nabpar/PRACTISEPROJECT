# Generated by Django 4.0.3 on 2022-04-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_prg_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='prg',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# Generated by Django 3.0.1 on 2020-01-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0002_auto_20200105_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localizacao',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='localizacao',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

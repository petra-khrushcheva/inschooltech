# Generated by Django 4.2.5 on 2023-09-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='indicatorsmetric',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='metric',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

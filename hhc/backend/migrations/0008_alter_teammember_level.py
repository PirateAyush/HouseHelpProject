# Generated by Django 4.2.1 on 2024-01-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_teammember_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='level',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
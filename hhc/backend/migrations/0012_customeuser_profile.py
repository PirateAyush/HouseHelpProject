# Generated by Django 4.2.1 on 2024-01-31 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_alter_feedback_blog_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='backend/users/profiles'),
        ),
    ]

# Generated by Django 4.2.1 on 2024-01-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_feedback_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='backend/team_profiles/')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('facebook_profile', models.URLField(blank=True, max_length=500, null=True)),
                ('twitter_profile', models.URLField(blank=True, max_length=500, null=True)),
                ('linkedin_profile', models.URLField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
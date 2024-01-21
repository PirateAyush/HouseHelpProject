# Generated by Django 4.2.1 on 2024-01-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_service_additional_content_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='backend/feedback_and_comments/profiles')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
# Generated by Django 4.2.1 on 2024-01-26 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_teammember_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=255)),
                ('blog_image', models.ImageField(upload_to='backend/blogs/images')),
                ('blog_description_1', models.TextField()),
                ('blog_description_2', models.TextField()),
                ('uploaded_by', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='blog_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='backend.blog'),
        ),
    ]
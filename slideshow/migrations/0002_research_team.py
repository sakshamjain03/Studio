# Generated by Django 5.0.2 on 2024-04-17 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slideshow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Research/images')),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team/images')),
            ],
        ),
    ]

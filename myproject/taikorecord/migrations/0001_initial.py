# Generated by Django 4.0.5 on 2022-06-25 03:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='難易度')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='ジャンル')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.CharField(max_length=100, verbose_name='曲名')),
                ('result_date', models.DateField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music', to='taikorecord.genre', verbose_name='ジャンル')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log', to='taikorecord.music', verbose_name='曲名')),
            ],
        ),
    ]

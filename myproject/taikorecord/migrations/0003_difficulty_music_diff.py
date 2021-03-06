# Generated by Django 4.0.5 on 2022-06-25 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taikorecord', '0002_delete_difficulty_rename_music_music_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=10, verbose_name='難易度')),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='diff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='music', to='taikorecord.difficulty', verbose_name='難易度'),
            preserve_default=False,
        ),
    ]

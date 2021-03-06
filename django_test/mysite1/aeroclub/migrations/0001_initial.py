# Generated by Django 2.2.2 on 2019-06-19 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AeroClub',
            fields=[
                ('club_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('club_name', models.CharField(max_length=255)),
                ('club_secretary', models.CharField(max_length=255)),
                ('club_status', models.CharField(choices=[('A', 'Active'), ('INA', 'Inactive')], default='INA', max_length=2)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_of_club', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('post_content', models.CharField(max_length=2000)),
                ('post_likes', models.IntegerField(default=0)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aeroclub.AeroClub')),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aeroclub.Post')),
            ],
        ),
    ]

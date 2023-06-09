# Generated by Django 4.2.1 on 2023-05-21 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_alter_userrants_ranttext'),
    ]

    operations = [
        migrations.CreateModel(
            name='userFollowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followingList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followedUser', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-19 14:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0002_feed_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
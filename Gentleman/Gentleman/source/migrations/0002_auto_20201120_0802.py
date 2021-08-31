# Generated by Django 3.1.3 on 2020-11-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredarticle',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='featuredpodcast',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='topstories',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
# Generated by Django 2.2.7 on 2019-11-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filmID', models.IntegerField()),
                ('title', models.CharField(max_length=120)),
                ('genre', models.CharField(max_length=12)),
                ('releaseYear', models.CharField(max_length=4)),
                ('length', models.IntegerField()),
                ('MPAA_rating', models.CharField(max_length=6)),
                ('qualityRating', models.IntegerField()),
            ],
        ),
    ]
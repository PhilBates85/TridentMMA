# Generated by Django 2.2.3 on 2019-11-24 00:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_category', models.CharField(max_length=200)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_slug', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_series', models.CharField(max_length=200)),
                ('series_summary', models.CharField(max_length=200)),
                ('tutorial_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialCategory', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.CharField(max_length=200)),
                ('tutorial_content', models.TextField()),
                ('tutorial_published', models.DateTimeField(default=datetime.datetime(2019, 11, 23, 18, 37, 5, 462335), verbose_name='date published')),
                ('tutorial_slug', models.CharField(default=1, max_length=200)),
                ('tutorial_series', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialSeries', verbose_name='Series')),
            ],
        ),
    ]

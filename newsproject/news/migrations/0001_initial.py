# Generated by Django 5.0.7 on 2024-07-27 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_headline', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('news_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.newscategory')),
            ],
        ),
    ]

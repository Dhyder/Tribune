# Generated by Django 3.2.9 on 2021-11-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_post_date_article_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='articles/'),
        ),
    ]

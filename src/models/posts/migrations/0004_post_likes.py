# Generated by Django 2.1.7 on 2019-03-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20190224_1010'),
        ('posts', '0003_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='profile.Profile'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-02-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20190224_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]

0# Generated by Django 3.2.9 on 2021-12-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuevaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]

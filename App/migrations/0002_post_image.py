# Generated by Django 3.2.4 on 2021-06-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]

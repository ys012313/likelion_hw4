# Generated by Django 2.2.2 on 2019-06-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_post_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/default_image.jpeg', upload_to=''),
        ),
    ]

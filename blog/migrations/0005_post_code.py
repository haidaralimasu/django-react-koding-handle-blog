# Generated by Django 3.1.7 on 2021-03-28 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='code',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

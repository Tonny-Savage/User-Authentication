# Generated by Django 3.1 on 2020-10-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_auto_20201025_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]

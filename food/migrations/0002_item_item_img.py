# Generated by Django 4.1.3 on 2022-12-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_img',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/512/1147/1147805.png', max_length=500),
        ),
    ]

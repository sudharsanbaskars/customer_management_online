# Generated by Django 3.2.3 on 2021-06-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210628_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]

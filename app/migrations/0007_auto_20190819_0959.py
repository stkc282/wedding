# Generated by Django 2.1.3 on 2019-08-19 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190819_0900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'name', 'verbose_name_plural': 'name'},
        ),
    ]
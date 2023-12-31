# Generated by Django 4.2.1 on 2023-07-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_alter_checkout_user_alter_houses_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='description',
            field=models.CharField(choices=[('bedsitter', ' bedsitter'), ('two bedroom', 'two bedroom'), ('three bedroom', 'three bedroom'), ('four bedroom', 'four bedroom')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='name',
            field=models.CharField(blank=True, choices=[('bedsitter', ' bedsitter'), ('two bedroom', 'two bedroom'), ('three bedroom', 'three bedroom'), ('four bedroom', 'four bedroom')], max_length=100, null=True),
        ),
    ]

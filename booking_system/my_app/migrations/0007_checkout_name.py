# Generated by Django 4.2.1 on 2023-06-25 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_remove_checkout_name_alter_checkout_date_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.customer'),
        ),
    ]

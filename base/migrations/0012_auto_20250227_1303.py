# Generated by Django 3.2.19 on 2025-02-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_tickets_ticket_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='route',
            new_name='arrival_city',
        ),
        migrations.AddField(
            model_name='bus',
            name='departure_city',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.19 on 2025-02-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20250218_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='amount',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

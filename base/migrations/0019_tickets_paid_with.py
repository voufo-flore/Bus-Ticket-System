# Generated by Django 3.2.19 on 2025-02-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20250227_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='paid_with',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

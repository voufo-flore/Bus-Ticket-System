# Generated by Django 3.2.19 on 2025-02-28 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_remove_tickets_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.user'),
            preserve_default=False,
        ),
    ]

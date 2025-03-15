# Generated by Django 3.2.19 on 2025-02-18 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_payment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='agency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.agency'),
            preserve_default=False,
        ),
    ]

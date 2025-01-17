# Generated by Django 5.1.4 on 2024-12-19 12:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='Reg_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]

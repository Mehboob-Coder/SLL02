# Generated by Django 5.1.4 on 2024-12-19 12:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_id_alter_user_reg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Reg_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
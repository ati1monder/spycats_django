# Generated by Django 5.1.3 on 2024-11-19 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_target_mission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.spycat'),
        ),
        migrations.AlterField(
            model_name='target',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='api.mission'),
        ),
    ]

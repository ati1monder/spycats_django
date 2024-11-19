# Generated by Django 5.1.3 on 2024-11-19 15:42

import api.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpyCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('years_of_experience', models.PositiveIntegerField(verbose_name='Years of experience')),
                ('breed', models.CharField(max_length=50, validators=[api.validators.breed_validation], verbose_name='Breed')),
                ('salary', models.IntegerField(verbose_name='Salary')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.spycat')),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('notes', models.TextField(max_length=500, verbose_name='Notes')),
                ('complete', models.BooleanField(default=False)),
                ('mission', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='api.mission')),
            ],
        ),
    ]
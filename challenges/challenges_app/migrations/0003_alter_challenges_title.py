# Generated by Django 5.0.1 on 2024-01-31 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges_app', '0002_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
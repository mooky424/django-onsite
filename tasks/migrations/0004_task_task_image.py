# Generated by Django 5.0.2 on 2024-04-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_options_alter_task_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_image',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
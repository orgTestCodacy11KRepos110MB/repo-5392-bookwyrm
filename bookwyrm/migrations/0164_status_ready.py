# Generated by Django 3.2.16 on 2022-11-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0163_merge_0160_auto_20221101_2251_0162_importjob_task_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="status",
            name="ready",
            field=models.BooleanField(default=True),
        ),
    ]

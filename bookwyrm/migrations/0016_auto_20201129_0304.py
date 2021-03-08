# Generated by Django 3.0.7 on 2020-11-29 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.fields import ArrayField


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0015_auto_20201128_0349"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="subject_places",
            field=ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="subjects",
            field=ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="edition",
            name="parent_work",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="editions",
                to="bookwyrm.Work",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name="tag",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="tag",
            name="book",
        ),
        migrations.RemoveField(
            model_name="tag",
            name="user",
        ),
        migrations.CreateModel(
            name="UserTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("remote_id", models.CharField(max_length=255, null=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="bookwyrm.Edition",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="bookwyrm.Tag"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "book", "tag")},
            },
        ),
    ]

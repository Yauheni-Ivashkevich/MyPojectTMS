# Generated by Django 3.0.6 on 2020-05-11 13:58

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                ("name", models.TextField(blank=True, null=True)),
                ("position", models.TextField(blank=True, null=True)),
                ("started_at", models.DateField(blank=True, null=True)),
                ("finished_at", models.DateField(blank=True, null=True)),
                ("achievements_text", models.TextField(blank=True, null=True)),
                ("link", models.TextField(blank=True, null=True)),
            ],
            options={"verbose_name_plural": "Organizations",},
        ),
        migrations.CreateModel(
            name="ResumePage",
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
                ("title", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={"verbose_name_plural": "Resume Page",},
        ),
        migrations.CreateModel(
            name="Responsibility",
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
                ("summary", models.TextField()),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responsibilities",
                        to="resume.Organization",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Responsibilities",},
        ),
    ]

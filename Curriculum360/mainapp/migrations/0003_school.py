# Generated by Django 4.2 on 2023-05-31 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_delete_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="school",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("school_name", models.CharField(max_length=300)),
                ("about", models.TextField()),
                ("blog", models.TextField()),
                ("department", models.ManyToManyField(to="mainapp.department")),
            ],
        ),
    ]
# Generated by Django 4.2 on 2023-05-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_school"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="blog",
            field=models.TextField(default=models.TextField()),
        ),
        migrations.CreateModel(
            name="semister",
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
                ("semister_number", models.IntegerField()),
                ("year", models.IntegerField()),
                ("courses", models.ManyToManyField(to="mainapp.course")),
            ],
        ),
        migrations.AlterField(
            model_name="department",
            name="course_list",
            field=models.ManyToManyField(to="mainapp.semister"),
        ),
    ]

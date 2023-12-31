# Generated by Django 4.2.4 on 2023-09-07 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=60)),
                ("description", models.TextField(blank=True, null=True)),
                ("publication_date", models.DateField(null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.author",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookTag",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Fiction", "Fiction"),
                            ("Fantasy", "Fantasy"),
                            ("Comedy", "Comedy"),
                            ("Adventure", "Adventure"),
                            ("Romance", "Romance"),
                            ("Sci-Fi", "Scifi"),
                            ("History", "History"),
                        ],
                        max_length=15,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="BookInventory",
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
                ("stock_quantity", models.PositiveIntegerField()),
                (
                    "name",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="main.book"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookImage",
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
                ("cover_image", models.ImageField(upload_to="book-covers")),
                (
                    "thumbnail",
                    models.ImageField(
                        editable=False, null=True, upload_to="book-thumbnails"
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.book"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="tags",
            field=models.ManyToManyField(blank=True, to="main.booktag"),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_author_bookimage_bookinventory_booktag_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booktag",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
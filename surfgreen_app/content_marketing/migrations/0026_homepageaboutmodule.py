# Generated by Django 4.1.9 on 2023-09-16 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("content_marketing", "0025_homepageheromodule"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomepageAboutModule",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="%(app_label)s_%(class)s",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="offer_service_module")),
                ("image_title", models.CharField(blank=True, max_length=255, null=True)),
                ("image_alt_text", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]

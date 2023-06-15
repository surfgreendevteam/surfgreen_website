# Generated by Django 4.1.9 on 2023-05-20 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("content_marketing", "0006_getintouchmodule"),
    ]

    operations = [
        migrations.CreateModel(
            name="FooterModule",
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
                ("contact_title", models.CharField(blank=True, max_length=255, null=True)),
                ("phone_number", models.CharField(blank=True, max_length=255, null=True)),
                ("email_adress", models.CharField(blank=True, max_length=255, null=True)),
                ("street_adress", models.CharField(blank=True, max_length=255, null=True)),
                ("city_adress", models.CharField(blank=True, max_length=255, null=True)),
                ("linkedin_link", models.CharField(blank=True, max_length=255, null=True)),
                ("instagram_link", models.CharField(blank=True, max_length=255, null=True)),
                ("seo_text", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]

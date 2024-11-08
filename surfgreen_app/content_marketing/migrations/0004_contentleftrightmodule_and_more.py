# Generated by Django 4.1.9 on 2023-05-19 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("content_marketing", "0003_howweworkitem_howweworkmodule"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContentLeftRightModule",
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
                ("link", models.CharField(blank=True, max_length=255, null=True)),
                ("link_title", models.CharField(blank=True, max_length=255, null=True)),
                ("image_is_left", models.BooleanField(default=True)),
                ("image_title", models.CharField(blank=True, max_length=255, null=True)),
                ("image_alt_text", models.CharField(blank=True, max_length=255, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="content_left_right_module")),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
        migrations.AddField(
            model_name="offerservicemodule",
            name="image_alt_text",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="offerservicemodule",
            name="image_title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 4.1.9 on 2024-11-16 08:46

from django.db import migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):
    dependencies = [
        ("content_marketing", "0026_homepageaboutmodule"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursedetail",
            name="course_author_description",
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="coursedetail",
            name="course_description",
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="coursedetail",
            name="short_description",
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.9 on 2023-08-28 09:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("content_marketing", "0015_coursedetail_duration_coursedetail_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coursedetailcontent",
            name="course",
        ),
        migrations.RemoveField(
            model_name="coursedetailwhatyoulearnitem",
            name="course",
        ),
    ]

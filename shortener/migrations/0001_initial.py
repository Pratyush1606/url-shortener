# Generated by Django 4.1.7 on 2023-02-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Url",
            fields=[
                (
                    "url_id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("original_url", models.URLField()),
                ("short_url", models.CharField(max_length=15, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("expires_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]

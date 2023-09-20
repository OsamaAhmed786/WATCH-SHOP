# Generated by Django 4.2.1 on 2023-09-20 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("watch", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=100)),
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("massage", models.TextField()),
                (
                    "Category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="watch.category"
                    ),
                ),
                (
                    "Product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="watch.product"
                    ),
                ),
            ],
        ),
    ]
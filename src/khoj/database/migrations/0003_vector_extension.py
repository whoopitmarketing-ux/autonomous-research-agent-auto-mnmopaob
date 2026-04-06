from django.db import migrations
from pgvector.django import VectorExtension


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0002_googleuser"),
    ]

    operations = [
        VectorExtension(
            name="vector",
            dim=128,
            index_type="GIN",
            index_params={
                "gin_pending_list_limit": 10000,
            },
        ),
    ]
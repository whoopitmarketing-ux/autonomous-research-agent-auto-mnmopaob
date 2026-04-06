import logging
from typing import List

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Q
from tqdm import tqdm

from khoj.database.adapters import get_default_search_model
from khoj.database.models import Entry, SearchModelConfig
from khoj.processor.embeddings import EmbeddingsModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BATCH_SIZE = 1000  # Define an appropriate batch size

class Command(BaseCommand):
    help = "Convert all existing Entry objects to use a new default Search model."

    def handle(self, *args, **options):
        search_model = get_default_search_model()
        entries = Entry.objects.all()
        with transaction.atomic():
            for i in tqdm(range(0, entries.count(), BATCH_SIZE)):
                batch = entries[i:i+BATCH_SIZE]
                batch.update(search_model=search_model)
                batch.save()
        logger.info("Default search model updated successfully.")

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Simulate the update without making any changes.",
        )

    def execute(self, *args, **options):
        if options.get("dry_run"):
            logger.info("Dry run enabled. No changes will be made.")
        return super().execute(*args, **options)
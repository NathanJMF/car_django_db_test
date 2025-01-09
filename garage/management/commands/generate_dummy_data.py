from django.core.management.base import BaseCommand
from dummy_data_factory.populate_data_base import populate_dummy_data


class Command(BaseCommand):
    help = "Populates the database with dummy data."

    def handle(self, *args, **options):
        results = populate_dummy_data()
        self.stdout.write(self.style.SUCCESS(f"Completed Dummy Data Generation: {results}"))

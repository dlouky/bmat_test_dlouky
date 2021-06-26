from django.core.management.base import BaseCommand, CommandError

from bmat_app.utils.file_to_db import import_from_csv


class Command(BaseCommand):
    help = "Imports metadata from a csv file to create the Works Single View"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            nargs=1,
            type=str,
            help="csv file with metadata to create the Works Single View",
        )

    def handle(self, *args, **kwargs):
        filename = kwargs["csv_file"][0]

        try:
            with open(filename, "r") as csv_file:
                import_from_csv(csv_file)
        except (IOError, OSError):
            raise CommandError('File "%s" does not exist' % filename)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully imported from {filename}!!")
        )

import csv
import os

from django.core import management
from django.core.management.base import CommandError
from django.test import TestCase

from bmat_app.models import MusicalWork

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def create_test_metadata():
    """
    Creates a CSV with metadata to test and returns a list of
    dictionaries with the metadata to test.
    """
    test_metadata = [
        {
            "title": "test_title1",
            "contributors": "test1_contrib1|test1_contrib2",
            "iswc": "test1111111",
        },
        {
            "title": "test_title2",
            "contributors": "test2_contrib1",
            "iswc": "test2222222",
        },
    ]
    keys = test_metadata[0].keys()
    with open(BASE_DIR + "/test_metadata.csv", "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(test_metadata)

    return test_metadata


class TestCommands(TestCase):
    def test_import_csv(self):

        # Test CommandError when a wrong CSV is provided
        with self.assertRaises(CommandError) as error_msg:
            management.call_command("import_csv", "wrong.csv")
        self.assertEqual(
            error_msg.exception.__str__(), 'File "wrong.csv" does not exist!!'
        )

        # Empty database running the first time
        assert MusicalWork.objects.count() == 0

        # Create metadata for testing purposes
        test_metadata = create_test_metadata()

        # Import the CSV with metadata to test
        management.call_command("import_csv", BASE_DIR + "/test_metadata.csv")

        # A total of 2 works should have been imported
        assert MusicalWork.objects.count() == 2

        for work_tm in test_metadata:
            work_db = MusicalWork.objects.get(title=work_tm["title"]).__dict__
            work_db.pop("_state")
            work_db.pop("uid")
            work_tm["contributors"] = work_tm["contributors"].split("|")
            assert work_db == work_tm

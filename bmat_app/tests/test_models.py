import os

from django.test import TestCase

from bmat_app.models import MusicalWork

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# models test
class MusicalWorkTest(TestCase):
    def create_musical_work(
        self,
        title="test0",
        contributors=["test0_contrib1", "test0_contrib2"],
        iswc="test0000000",
    ):
        return MusicalWork.objects.create(
            title=title, contributors=contributors, iswc=iswc
        )

    def test_musical_work_creation(self):
        work = self.create_musical_work()
        self.assertTrue(isinstance(work, MusicalWork))
        self.assertEqual(work.__str__(), work.title)

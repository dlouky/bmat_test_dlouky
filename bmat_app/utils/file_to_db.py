import csv
from django.db.models import Q
from bmat_app.models import MusicalWork


def work_from_db(metadata):
    """
    Returns a MusicalWork from db if:
        1-ISWC in db is the same in metadata or
        2-title and contributors in db are the same in metadata
    """

    return MusicalWork.objects.filter(
        Q(iswc=metadata["iswc"])
        | Q(title=metadata["title"], contributors=metadata["contributors"])
    ).first()


def reconcile_work(musical_work, metadata):
    """
    Completes data in musical_work with data present in metadata.
    """

    for attr in ["title", "iswc"]:
        if not getattr(musical_work, attr):
            setattr(musical_work, attr, metadata[attr])
    musical_work.contributors.extend(
        x for x in metadata["contributors"] if x not in musical_work.contributors
    )
    musical_work.save()


def import_from_csv(csv_file):
    """
    Read the input ﬁle, detect duplicate musical works and store reconciled
    works in the database.
    """
    rows = csv.reader(csv_file, delimiter=",")
    row0 = set(next(rows))
    if row0 != set(['title', 'contributors', 'iswc']):
        csv_file.seek(0)
        
    

    for row in rows:
        metadata = {
            "title": row[0],
            "contributors": row[1].split("|"),
            "iswc": row[2],
        }
        musical_work = work_from_db(metadata)
        if musical_work:
            reconcile_work(musical_work, metadata)
        else:
            musical_work = MusicalWork.objects.create(**metadata)

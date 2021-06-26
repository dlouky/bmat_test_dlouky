from django.db.models import Q

from bmat_app.models import MusicalWork


def work_from_db(metadata: dict):
    """
    Returns a MusicalWork from db if:
        1-ISWC in db is the same in metadata or
        2-title and at least a contributor in db are the same in metadata
    """

    return MusicalWork.objects.filter(
        Q(iswc=metadata["iswc"], iswc__isnull=False)
        | Q(title=metadata["title"], contributors__overlap=metadata["contributors"])
    ).first()


def work_reconciliation(musical_work: MusicalWork, metadata: dict):
    """
    Completes data in musical_work with data present in metadata.
    """

    for attr in ["title", "iswc"]:
        if not getattr(musical_work, attr):
            setattr(musical_work, attr, metadata[attr])
    musical_work.contributors.extend(
        set(metadata["contributors"]) - set(musical_work.contributors)
    )
    musical_work.save()


def work_to_db(metadata: dict):
    """
    Reconcile work with metadata if works exists in db, else create
    a new work in the db.
    """
    musical_work = work_from_db(metadata)
    if musical_work:
        work_reconciliation(musical_work, metadata)
    else:
        musical_work = MusicalWork.objects.create(**metadata)

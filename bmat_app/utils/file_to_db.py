import csv

from .work_flow import work_to_db


def import_from_csv(csv_file):
    """
    Read the input ﬁle, detect duplicate musical works and store reconciled
    works in the database. If work doesn't exists it is created.
    """
    rows = csv.reader(csv_file, delimiter=",")
    row0 = set(next(rows))
    if row0 != set(["title", "contributors", "iswc"]):
        csv_file.seek(0)

    for row in rows:
        metadata = {
            "title": row[0],
            "contributors": row[1].split("|"),
            "iswc": row[2],
        }
        work_to_db(metadata)

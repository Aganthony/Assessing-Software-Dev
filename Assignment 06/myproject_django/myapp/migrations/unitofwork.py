# unitofwork.py

from contextlib import contextmanager
from django.db import transaction
from .models import Bookmark

class UnitOfWork:
    def __init__(self):
        self.bookmarks = BookmarkRepository()

    def __enter__(self):
        # Start a new transaction
        self.txn = transaction.atomic()
        self.txn.__enter__()
        return self

    def __exit__(self, *args):
        # Commit or rollback the transaction
        self.txn.__exit__(*args)

    def commit(self):
        # Placeholder for commit if needed
        pass

    def rollback(self):
        # Placeholder for rollback if needed
        pass

class BookmarkRepository:
    def add(self, bookmark: Bookmark):
        bookmark.save()

    def get(self, bookmark_id):
        return Bookmark.objects.get(id=bookmark_id)

    def list(self):
        return list(Bookmark.objects.all())

    def remove(self, bookmark_id):
        bookmark = self.get(bookmark_id)
        bookmark.delete()

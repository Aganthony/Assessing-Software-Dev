from django.test import TestCase
from django.utils import timezone
from myapp.models import Bookmark


class BookmarkModelTest(TestCase):

    def test_saving_and_retrieving_bookmarks(self):
        first_bookmark = Bookmark()
        first_bookmark.title = "The first (ever) bookmark"
        first_bookmark.url = "http://example.com"
        first_bookmark.notes = "This is a test bookmark."
        first_bookmark.date_added = timezone.now()
        first_bookmark.save()

        saved_bookmarks = Bookmark.objects.all()
        self.assertEqual(saved_bookmarks.count(), 1)

        first_saved_bookmark = saved_bookmarks[0]
        self.assertEqual(first_saved_bookmark.title, "The first (ever) bookmark")
        self.assertEqual(first_saved_bookmark.url, "http://example.com")

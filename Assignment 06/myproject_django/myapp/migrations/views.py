from django.http import HttpResponse
from .models import Bookmark

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    bookmarks_list = ', '.join([bookmark.title for bookmark in bookmarks])
    return HttpResponse(bookmarks_list)

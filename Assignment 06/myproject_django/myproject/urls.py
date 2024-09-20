from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def temporary_view(request):
    return HttpResponse("Temporary Response")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmarks/', temporary_view),
]

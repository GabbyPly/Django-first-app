from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("phonebook/", include("phonebook.urls")),
    path("polls/", include("polls.urls")),
    path("base", include("base.urls")),
    path("admin/", admin.site.urls),
]

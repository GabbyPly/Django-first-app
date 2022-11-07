from django.contrib import admin
from django.urls import include, path
from django.urls import path, include


urlpatterns = [
    path("", include("phonebook.urls")),
    path("polls/", include("polls.urls")),
    path("base", include("base.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]

from django.urls import path

from . import views

app_name = "phonebook"
urlpatterns = [
    path("", views.goto, name="homepage"),
    path("phonebook/", views.homepage, name="homepage"),
]

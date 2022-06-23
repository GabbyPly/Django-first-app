from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "phonebook"
urlpatterns = [
    path("phonebook/", views.ConatctList.as_view()),
    path("phonebook/<int:pk>/", views.ConatctDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

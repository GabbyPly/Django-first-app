from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "phonebook"
urlpatterns = [
    path("", views.api_root),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path("phonebook/<int:pk>/highlight/", views.ContactHighlight.as_view()),
    path("phonebook/", views.ContactList.as_view()),
    path("phonebook/<int:pk>/", views.ConatctDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

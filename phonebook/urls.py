from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from phonebook import views

# API endpoints
urlpatterns = format_suffix_patterns(
    [
        path("", views.api_root),
        path("contacts/", views.ContactList.as_view(), name="contact-list"),
        path("contacts/<int:pk>/", views.ConatctDetail.as_view(), name="contact-detail"),
        path("contacts/<int:pk>/highlight/", views.ContactHighlight.as_view(), name="contact-highlight"),
        path("users/", views.UserList.as_view(), name="user-list"),
        path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    ]
)

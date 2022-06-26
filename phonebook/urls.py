from collections import UserList
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from phonebook import views
from phonebook.views import ContactViewSet, UserViewSet, api_root
from rest_framework import renderers

contact_list = ContactViewSet.as_view({"get": "list", "post": "create"})

contact_detail = ContactViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

contact_highlight = ContactViewSet.as_view({"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({"get": "list"})
user_detail = UserViewSet.as_view({"get": "retrieve"})

# API endpoints
urlpatterns = format_suffix_patterns(
    [
        path("", views.api_root),
        path("contacts/", contact_list, name="contact-list"),
        path("contacts/<int:pk>/", contact_detail, name="contact-detail"),
        path("contacts/<int:pk>/highlight/", contact_highlight, name="contact-highlight"),
        path("users/", user_list, name="user-list"),
        path("users/<int:pk>/", user_detail, name="user-detail"),
    ]
)

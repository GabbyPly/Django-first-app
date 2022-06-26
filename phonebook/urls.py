from django.urls import path, include
from rest_framework.routers import DefaultRouter
from phonebook import views


router = DefaultRouter()
router.register(r"contacts", views.ContactViewSet, basename="contacts")
router.register(r"users", views.UserViewSet, basename="users")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]

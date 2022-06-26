from django.urls import path, include
from rest_framework.routers import DefaultRouter
from phonebook import views

# basename is breaking
router = DefaultRouter()
router.register(
    r"contacts",
    views.ContactViewSet,
)
router.register(
    r"users",
    views.UserViewSet,
)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]

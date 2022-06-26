from django.urls import path, include
from rest_framework.routers import DefaultRouter
from phonebook import views

# basename is breaking
# If you want to include the basename use user & contact.
# The reason is probably: that they need to match the start of the internal view's name
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

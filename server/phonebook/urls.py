from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from phonebook import views


router = DefaultRouter()
router.register(r"contacts", views.ContactViewSet, basename="contact")
router.register(r"register", views.RegisterViewSet, basename="user")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path("login/", views.LoginView.as_view()),
]

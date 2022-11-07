from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from phonebook import views
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r"contacts", views.ContactViewSet, basename="contact")
router.register(r"posts", views.PostViewSet, basename="post")
router.register(r"users", views.UserViewSet, basename="user")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path("login/", views.LoginView.as_view()),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]

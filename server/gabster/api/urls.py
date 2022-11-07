from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("phonebook/contacts/", views.getStuff),
    # path('rooms/<str:pk>/', views.getRoom),
]

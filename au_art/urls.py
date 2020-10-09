from django.urls import path, include
from au_art.views import InitialView
from . import views

urlpatterns = [
    path("homepage", views.homepage, name="homepage")
]
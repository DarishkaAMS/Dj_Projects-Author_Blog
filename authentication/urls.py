from django.urls import path

from . import views

from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path("", views.index, name="indeX"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
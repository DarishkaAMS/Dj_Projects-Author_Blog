from django.urls import path, include
from au_art.views import InitialView
from . import views

urlpatterns = [
    path("homepage", views.homepage, name="homepage"),
    path("user", views.user, name="user"),
    path("<int:article_id>", views.article, name="article"),
    # path("<int:article_id>/join", views.join, name="join"),
]
from django.urls import path
from au_art.views import InitialView

urlpatterns = [
    path('', InitialView.as_view(), name='au_art')
]
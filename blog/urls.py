from django.urls import path

from . import views
from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('ajax/load-teams/', views.load_teams, name='ajax_load_teams'), # AJAX
]

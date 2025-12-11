# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("", views.home_view, name="home"),
    path("card/<int:slot>/", views.card_detail, name="card-detail"),
    path("logout/", views.logout_view, name="logout"),
]

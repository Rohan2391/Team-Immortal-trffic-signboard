from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("reset_password/", views.reset_password, name="reset_password"),
    path("home/", views.home, name="home"),  # Example home view
]

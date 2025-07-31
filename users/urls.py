from django.urls import path, reverse_lazy
from recipe import views

from users import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
    path("", views.recipe, name="index"),
    path("login/", user_view.user_login, name="login"),
    path("logout/", auth.LogoutView.as_view(next_page=reverse_lazy('index')), name="logout"),
    path("signup/", user_view.signup, name="signup"),
    path("settings/", user_view.settings, name="settings")
]
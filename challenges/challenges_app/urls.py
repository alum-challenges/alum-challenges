from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("problem_list", views.problem_list, name="problem_list"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("account", views.account_view, name="account"),
    path("problems/<str:title>", views.problem_view, name="problems"),
]

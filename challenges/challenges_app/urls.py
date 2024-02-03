from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("account", views.account_view, name="account"),
    path("problems/<str:title>", views.problem_view, name="problems"),
    path("search/", views.search, name="search-problems"),
    path("submit/new-problem", views.add_problem, name="add-problem"),
    path("about/", views.about_page, name="about"),
]

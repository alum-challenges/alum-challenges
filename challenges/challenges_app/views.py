from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import markdown
from .models import User
from . import util


def index(request):
    print(util.list_entries())
    return render(request, "index.html", {"problems": util.list_entries()})


def login_view(request):
    if request.method == "POST":
        # Attempt to sign in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication is successful
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(
                request,
                "accounts/login.html",
                {"message": "Invalid username and/or password."},
            )
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("index")


def signup_view(request):
    if request.method == "POST":
        nickname = str(request.POST.get("nickname"))
        password = str(request.POST.get("password"))
        confirm = str(request.POST.get("confirm"))

        if len(nickname) < 3:
            return render(
                request,
                "accounts/signup.html",
                {"message": "Nickname must be at least 3 characters long."},
            )
        elif password != confirm:
            return render(
                request,
                "accounts/signup.html",
                {"message": "Passwords you have entered must be the same."},
            )
        elif len(password) < 8:
            return render(
                request,
                "accounts/signup.html",
                {"message": "Password must be at least 8 characters long"},
            )

        user = User(nickname=nickname)
        user.set_password(password)
        user.save()

        return redirect("login")

    return render(request, "accounts/signup.html")


def problem_view(request, title):
    md = util.get_entry(title)

    if md == None:
        pass
    html = markdown.markdown(
        md,
        extensions=[
            "pymdownx.superfences",
            "pymdownx.highlight",
            "pymdownx.arithmatex",
            "pymdownx.magiclink",
        ],
    )
    return render(request, "problem.html", {"title": title, "problem": html})


@login_required
def account():
    return render(request, "account.html")

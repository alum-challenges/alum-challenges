from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    return render(
        request,
        "index.html",
    )


def login(request):
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


def logout(request):
    return render(request, "accounts/logout.html")


def signup(request):
    return render(request, "accounts/signup.html")

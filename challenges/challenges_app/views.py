from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
import markdown
from . import util
from challenges_app.models import Challenges
from django.db.utils import IntegrityError


# class ChallengesListView(ListView):
#     model = Challenges


def index(request):

    # util.paginate(request, QuerySet, amount of items per page)
    challenges = util.paginate(request, Challenges.objects.all().order_by("id"), 30)

    return render(
        request,
        "index.html",
        {"challenges": challenges},
    )


def problem_list(request):
    challenges = util.paginate(request, Challenges.objects.all().order_by("id"), 4)

    return render(
        request,
        "islands/problem_list.html",
        {"challenges": challenges},
    )


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
        username = request.POST["username"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]

        if len(username) < 3:
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
        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
            return render(
                request, "accounts/signup.html", {"message": "Username taken"}
            )

        login(request, user)
        return redirect("index")

    return render(request, "accounts/signup.html")


def problem_view(request, title):
    md = util.get_entry(title)
    if not md:
        return render(
            request,
            "error.html",
            {"title": title, "message": "This page does not exist"},
        )

    html = markdown.markdown(
        md,
        extensions=[
            "pymdownx.highlight",
            "pymdownx.superfences",
            "pymdownx.arithmatex",
            "pymdownx.magiclink",
            "pymdownx.blocks.details",
        ],
        extension_configs={
            "pymdownx.highlight": {
                # "pygments_style": "sas",
                # "linenums_style": "inline",
                "line_spans": "__codeline",
                "line_anchors": "__codelineno",
            },
        },
    )
    # meta = frontmatter(md)

    return render(
        request,
        "problem.html",
        {"title": util.get_challenge(title=title).full_title, "problem": html},
    )


@login_required
def account_view(request):
    return render(request, "accounts/account.html")

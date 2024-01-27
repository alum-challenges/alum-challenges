from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "accounts/login.html")

def logout(request):
    return render(request, "accounts/logout.html")

def signup(request):
    return render(request, "accounts/signup.html")
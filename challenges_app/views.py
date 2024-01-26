from django.shortcuts import render

def index(request):
    return render(request, "challenges_app/templates/index.html")
from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def Home(request):
    links = SocialMediaLinks.objects.first()
    if request.method == "POST":
        d = request.POST
        fullName = d["name"]
        email = d["email"]
        message = d["message"]
        ContactUs.objects.create(
            fullName=fullName, email=email, message=message)
        return redirect('/success')
    data = {
        "link": links
    }
    return render(request, 'Home.html', data)


def TeamPage(request):
    teamData = Team.objects.all()
    links = SocialMediaLinks.objects.first()
    data = {
        "item": teamData, "link": links
    }
    return render(request, "teamPage.html", data)


def SuccessPage(request):
    return render(request, "successMessage.html")

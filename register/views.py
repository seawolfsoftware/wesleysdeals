from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from deals.models import Deal


def home(response):

    deals = Deal.objects.all()

    if deals:
        return render(response, "main/home.html", {'deals': deals})
    else:
        return render(response, "main/home.html")


def register(request):
    if request.method == "POST":

        username = request.POST['email']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            print('User created')

        return redirect("/")
    else:
        return render(request, "registration/register.html")

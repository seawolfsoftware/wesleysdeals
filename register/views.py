from django.shortcuts import render, redirect
from .forms import RegisterForm

from posts.models import Post


def home(response):

    posts = Post.objects.all()

    return render(response, "main/home.html", {'posts': posts})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})

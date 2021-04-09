import random

from rest_framework import generics

from .models import Post, Subscribers
from .serializers import PostSerializer
from . import forms

from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.shortcuts import render
from django.db import IntegrityError
from wesleysdeals.settings import EMAIL_HOST_USER


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


@csrf_exempt
def new(request):
    try:
        if request.method == 'POST':
            sub = forms.Subscribe(request.POST)
            recipient = str(sub['Email'].value())
            sub2 = Subscribers.objects.create(email=recipient, conf_num=random_digits())

            subject = 'Welcome to Wesley\'s Deals & Steals!'
            message = 'Thank you for signing up to SAVE USING CODES! \
                        Please complete the process by clicking on the following link\
                        to confirm your registration. \
                        "{}confirm/?email={}&conf_num={}"'.format(
                request.build_absolute_uri('subscribe/'),
                sub2.email, sub2.conf_num)

            send_mail(subject, message, EMAIL_HOST_USER,
                      [recipient], fail_silently=False)

            recipient_list = Subscribers.objects.all()

            return render(request, 'subscribe/success.html',
                          {'recipient': recipient,
                           'recipient_list': recipient_list})
    except IntegrityError as e:
        return render(request, 'index.html', {'form': sub, "message": e.args})

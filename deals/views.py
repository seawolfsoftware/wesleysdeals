from rest_framework import generics

from .models import Deal
from .serializers import DealSerializer
from django.contrib.auth.models import User, Group


class DealList(generics.ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


class DealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


# def add_user_to_group():
#
#     group_name = "group{}".format(title)
#     new_multi_use_code_group, created = Group.objects.get_or_create(name=group_name)
#
#
#     user_group = Group.objects.get(name='Mygroup')
#
#     user.groups.add(user_group)



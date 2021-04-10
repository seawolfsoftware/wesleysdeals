from django.db import models
from django.contrib.auth.models import User, Group, Permission

from datetime import datetime, timedelta


class Deal(models.Model):

    # ForeignKey is a many-to-one relationship, many deals can be posted by one user
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return self.title


class MultiUseDeal(Deal):

    # access date time needs to be when the user accesses the deal, not when deal is posted

    access_datetime = models.DateTimeField(default=datetime.now)
    expiry_datetimestamp = datetime.now() + timedelta(minutes=15)
    expiry_date = models.DateTimeField(expiry_datetimestamp)

    @property
    def is_expired(self):
        if datetime.now > self.expiry_date:
            return True
        return False

    # is max_numbers of requests reached? if not,
    # initiate user into group where max size is max use times
    # one multi-use-code can be used by one group

    # new_multi_use_code_group, created = Group.objects.get_or_create(name='New Multi-Use Code Group')
    # permission_to_access = Permission.objects.get(name='Permission to access multi-use code')
    # new_multi_use_code_group.permissions.add(permission_to_access)
from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from datetime import datetime, timedelta


class Code(models.Model):
    code = models.TextField()


class Deal(models.Model):

    # ForeignKey is a many-to-one relationship, many deals can be posted by one user
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', default='default.jpg')
    is_multi_use = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('can_join_group', "Can join group"),

        )

    if is_multi_use:

        group_name = "group{}".format(title)
        new_multi_use_code_group, created = Group.objects.get_or_create(name=group_name)


    # ForeignKey is a many-to-one relationship, many codes can be posted by one deal
    code = models.ForeignKey(Code, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.title


# class MultiUseDeal(Deal):
#
# #
#     # access date time needs to be when the user accesses the deal, not when deal is posted
#
    # access_datetime = models.DateTimeField(default=datetime.now)
    # expiry_datetimestamp = datetime.now() + timedelta(minutes=15)
    # expiry_date = models.DateTimeField(expiry_datetimestamp)
#
#     @property
#     def is_expired(self):
#         if datetime.now > self.expiry_date:
#             return True
#         return False

    # is max_numbers of requests reached? if not,
    # initiate user into group where max size is max use times
    # one multi-use-code can be used by one group


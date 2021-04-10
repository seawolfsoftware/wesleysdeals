from rest_framework import serializers
from .models import Deal


class DealSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Deal

from django.urls import path

from .views import DealList, DealDetail

urlpatterns = [
    path('<int:pk>/', DealDetail.as_view(), name='DealDetail'),
    path('', DealList.as_view()),
]
from django.contrib import admin
from django.urls import include, path
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('', include("django.contrib.auth.urls")),
]

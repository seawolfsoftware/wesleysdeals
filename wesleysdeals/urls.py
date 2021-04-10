from django.contrib import admin
from django.urls import include, path
from register import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('deals.urls')),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('', include("django.contrib.auth.urls")),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
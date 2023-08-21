from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #django admin
    path('admin/', admin.site.urls),
    #user managment
    path('accounts/', include('allauth.urls')),
    #locac apps
    path('', include('pages.urls')),
    ]
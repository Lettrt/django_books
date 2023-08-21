from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #django admin
    path('admin/', admin.site.urls),
    #user managment
    path('accounts/', include('django.contrib.auth.urls')),
    #locac apps
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
    ]
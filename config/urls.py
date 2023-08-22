from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #django admin
    path('admin/', admin.site.urls),
    #user managment
    path('accounts/', include('allauth.urls')),
    #locac apps
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
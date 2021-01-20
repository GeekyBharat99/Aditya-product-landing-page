from django.contrib import admin
from django.urls import path
from landingpage.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="home"),
    path('team/', TeamPage, name="team"),
    path('success/', SuccessPage, name="success"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

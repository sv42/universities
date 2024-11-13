from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from sitepages import views

from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('next', views.next),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


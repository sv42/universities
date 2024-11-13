from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from sitepages import views

urlpatterns = [
    path('', views.show_file_content),
    path('about_us', views.about_us),  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



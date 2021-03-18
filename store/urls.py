from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('categories/', views.categories),
    path('post_ad/', views.post_ad),
    path('myads/', views.myads),
    path('ads/<int:category_id>/', views.ads)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
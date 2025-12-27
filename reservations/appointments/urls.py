from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'appointments'

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.allCars, name='allCars'),
    path('car/<int:pk>/', views.seeMore, name='seeMore'),
]
# obsluga media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

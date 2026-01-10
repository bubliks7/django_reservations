from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "rental"

urlpatterns = [
    path('create/<int:pk>', views.rezerwuj, name='rezerwuj'),
    path('myReservations/', views.mojeRezerwacje, name='mojeRezerwacje'),
    path('cancel/<int:pk>', views.anulujRezerwacje, name='anulujRezerwacje'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

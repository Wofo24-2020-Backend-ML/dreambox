
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('main.urls')),
    path('appointment_app/', include('appointment.urls')),
    path('csv_app/', include('csvapp.urls')),
]

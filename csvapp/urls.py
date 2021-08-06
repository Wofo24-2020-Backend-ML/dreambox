from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from csvapp import views
from django.urls import path, include



urlpatterns = [

    path('csvupload/', views.CSVDataView.as_view(), name='CSVDataView'),
]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

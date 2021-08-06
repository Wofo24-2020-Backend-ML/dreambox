from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

# router.register('booknow', AppointmentView)


urlpatterns = [
    #   path('', include(router.urls)),
    path('book/', NewAppointmentView.as_view(), name='NewAppointmentView'),
    path('mybooking/', MyAppointment.as_view(), name='MyAppointment'),
]

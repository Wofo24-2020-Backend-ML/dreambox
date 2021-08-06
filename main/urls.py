from django.urls import path
from .views import RegisterView, LoginAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginAPIView.as_view(), name="login"),
]

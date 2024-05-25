from django.urls import path
from .views import QRCodeView

urlpatterns = [
    path("", QRCodeView.as_view(), name="qr_code"),
]
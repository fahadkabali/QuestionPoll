from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="auditDashboard"),
    path('results/', views.results, name="auditResults"),
    path('download/pdf/', views.download_pdf, name="downloadPdf"),
    path('download/png/', views.download_png, name="downloadPng"),
]

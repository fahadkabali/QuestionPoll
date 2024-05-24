from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
    path('feedback/<int:response_id>/', views.feedback, name='feedback'),
]

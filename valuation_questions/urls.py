from django.urls import path
from . import views


app_name = 'valuation_questions'
urlpatterns = [
    path('', views.index, name ='index'),
    path('<int:question_id>/', views.detail, name ='detail'),
    path('<int:question_id>/results/', views.results, name ='results'),
    path('<int:question_id>/selection/', views.selection, name ='selection'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.fish_list, name='fish_list'),
    path('fish/<int:pk>/', views.fish_detail, name='fish_detail'),
    path('guide/', views.fish_keeping_guide, name='fish_keeping_guide'),
    path('pods/', views.fish_pods, name='fish_pods'),
    path('fishing-methods/', views.fishing_methods, name='fishing_methods'),
    path('preparations/', views.fish_preparations, name='fish_preparations'),
]

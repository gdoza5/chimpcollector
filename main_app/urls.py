from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chimps/', views.chimps_index, name='index'),
    path('chimps/<int:chimp_id>', views.chimps_detail, name='detail'),
]
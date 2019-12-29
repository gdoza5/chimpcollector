from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chimps/', views.chimps_index, name='index'),
    path('chimps/<int:chimp_id>', views.chimps_detail, name='detail'),
    path('chimps/create/', views.ChimpCreate.as_view(), name='chimps_create'),
    path('chimps/<int:pk>/update', views.ChimpUpdate.as_view(), name='chimps_update'),
    path('chimps/<int:pk>/delete', views.ChimpDelete.as_view(), name='chimps_delete'),
]
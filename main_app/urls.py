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
    path('chimps/<int:chimp_id>/add_shift/', views.add_shift, name='add_shift'),
    path('chimps/<int:chimp_id>/assoc_slingshot/<int:slingshot_id>/', views.assoc_slingshot, name='assoc_slingshot'),
    path('chimps/<int:chimp_id/unassoc_slingshot/<int:toy_id>/', views.unassoc_shlingshot, name='unassoc_toy'),
    path('slingshots/', views.SlingshotList.as_view(), name='slingshots_index'),
    path('slingshots/<int:pk>/', views.SlingshotDetail.as_view(), name='slingshot_detail'),
    path('slingshots/create/', views.SlingshotCreate.as_view(), name='slingshots_create'),
    path('slingshots/<int:pk>/update', views.SlingshotUpdate.as_view(), name='slingshots_update'),
    path('slingshots/<int:pk>/delete', views.SlingshotDelete.as_view(), name='slingshots_delete')
]
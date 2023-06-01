from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', lambda req: redirect('/china')),
    path('china', views.ChinaView.as_view(), name='china'),
    # path('province/<str:province>', views.ProvinceView.as_view(), name='province'),
    # path('province/<str:province>/<str:municipality>', views.ProvinceView.as_view(), name='municipality'),
    path('province/', views.ProvinceView.as_view(), name='province'),

    path('set_media', views.set_media, name='set_media'),
    path('get_data_from_feed', views.get_data_from_feed, name='get_data_from_feed'),

    # path('', views.index, name='index'),
]
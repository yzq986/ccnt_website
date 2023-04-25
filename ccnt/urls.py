from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', lambda req: redirect('/china')),
    path('china', views.ChinaView.as_view(), name='china'),
    path('province/<str:province>', views.ProvinceView.as_view(), name='province'),
    # path('', views.index, name='index'),
]
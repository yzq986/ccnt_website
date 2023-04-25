from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count, F
import flask
from .models import Data
import json
import pinyin


def index(request):
    datas = Data.objects.all()
    # 指定渲染模板并向模板传递数据
    return render(request, "index.html", { "data": datas,})

def china(request):
    # "select a['省级行政区'] as key, count(1) as cnt where a['省级行政区'] != '' and a['市级行政区'] == '' group by a['省级行政区']"
    datas = Data.objects.exclude(province='').filter(municipality='').values('province').annotate(cnt=Count('province')).order_by('province')
    return HttpResponse(datas)

from django.views.generic import ListView

class ChinaView(ListView):
    queryset = Data.objects.exclude(country='').filter(province='').order_by('-date_published', '-month_published')
    template_name = "ccnt/china.html"
    paginate_by = 20 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        map_data = list(Data.objects.exclude(province='').filter(municipality='').values('province').annotate(name=F('province'), value=Count('province')).values('name', 'value'))
        print(map_data)
        context['map_data'] = json.dumps(map_data)
        return context

class ProvinceView(ListView):
    template_name = "ccnt/province.html"
    paginate_by = 20 

    def get_queryset(self):
        return Data.objects.filter(province=self.kwargs["province"], municipality='').order_by('-date_published', '-month_published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        map_data = list(Data.objects.exclude(municipality='').filter(province=self.kwargs["province"]).values('municipality').annotate(name=F('municipality'), value=Count('municipality')).values('name', 'value'))

        province = self.kwargs["province"][:-1]
        province_en = pinyin.get(province, format="strip")
        
        context['map_data'] = json.dumps(map_data)
        context['province'] = json.dumps(province)
        context['province_en'] = json.dumps(province_en)
        context['province_en_url'] = json.dumps(f"https://assets.pyecharts.org/assets/v5/maps/{province_en}.js")
        return context




# def china(request):
#     # "select a['省级行政区'] as key, count(1) as cnt where a['省级行政区'] != '' and a['市级行政区'] == '' group by a['省级行政区']"
#     # datas = Data.objects.exclude(province='').filter(municipality='').values('province').annotate(cnt=Count('province')).order_by('province')
#     datas = Data.objects.exclude(country='').filter(province='')
#     return HttpResponse(datas)
    

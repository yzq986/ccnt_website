from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count, F
import flask
from .models import Data
import json
from pypinyin import pinyin, lazy_pinyin, Style
from .utils import *
import os


def index(request):
    datas = Data.objects.all()
    # 指定渲染模板并向模板传递数据
    return render(
        request,
        "index.html",
        {
            "data": datas,
        },
    )


def china(request):
    # "select a['省级行政区'] as key, count(1) as cnt where a['省级行政区'] != '' and a['市级行政区'] == '' group by a['省级行政区']"
    datas = Data.objects.exclude(province="").filter(municipality="").values("province").annotate(cnt=Count("province")).order_by("province")
    return HttpResponse(datas)

def set_all_images(request):
    browser = Browser()
    for data in Data.objects.filter(id__lt=627).all()[::-1]:
        if data.link:
            filename = browser.save(data.link, data.id)
            # data.link_image = filename + '.png'
            data.link_pdf = filename + '.pdf'
            if data.month_published is None or data.month_published == '':
                data.month_published = 1
            data.save()


from django.views.generic import ListView


class ChinaView(ListView):
    queryset = Data.objects.exclude(country="").filter(province="").order_by("-date_published", "-month_published")
    template_name = "ccnt/china.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        map_data = list(
            Data.objects.exclude(province="")
            .filter(municipality="")
            .values("province")
            .annotate(name=F("province"), value=Count("province"))
            .values("name", "value")
        )
        print(map_data)
        context["map_data"] = json.dumps(map_data)
        return context


class ProvinceView(ListView):
    template_name = "ccnt/province.html"
    paginate_by = 20

    def get_queryset(self):
        province = self.request.GET.get("province", None)
        municipality = self.request.GET.get('municipality', None)
        if municipality is None:
            return Data.objects.filter(province=province, municipality="").order_by("-date_published", "-month_published")
        else:
            return Data.objects.filter(municipality=municipality).order_by("-date_published", "-month_published")

    def get_context_data(self, **kwargs):
        province = self.request.GET.get("province", None)

        context = super().get_context_data(**kwargs)
        map_data = list(
            Data.objects.exclude(municipality="")
            .filter(province=province)
            .values("municipality")
            .annotate(name=F("municipality"), value=Count("municipality"))
            .values("name", "value")
        )
        print(Data.objects.exclude(municipality="")
            .filter(province=province))

        province = province[:2] if not province.startswith("黑龙江") and not province.startswith("内蒙古") else province[:3]
        province_en = ''.join(lazy_pinyin(province))

        context["map_data"] = json.dumps(map_data)
        context["province"] = json.dumps(province)
        context["province_en"] = json.dumps(province_en)
        context["province_en_url"] = json.dumps(f"https://assets.pyecharts.org/assets/v5/maps/{province_en}.js")
        return context


# def china(request):
#     # "select a['省级行政区'] as key, count(1) as cnt where a['省级行政区'] != '' and a['市级行政区'] == '' group by a['省级行政区']"
#     # datas = Data.objects.exclude(province='').filter(municipality='').values('province').annotate(cnt=Count('province')).order_by('province')
#     datas = Data.objects.exclude(country='').filter(province='')
#     return HttpResponse(datas)

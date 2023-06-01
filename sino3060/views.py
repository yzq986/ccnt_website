from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count, F
import flask
from .models import Data
import json
from pypinyin import pinyin, lazy_pinyin, Style
from .utils import *
import os
from .constant import *
from datetime import datetime
from time import mktime
# from dal import autocomplete

FEED_URL = "https://www.google.com/alerts/feeds/01155419682148081808/3691399718111468196"
DEEPL_API = "b953cf0e-4320-da53-93fc-da67f7efc047:fx"
# DEEPL_API = "123ef762-e73f-4ed2-8a68-5a1830bdce64:fx"

def set_all_media(request):
    browser = Browser()
    for data in Data.objects.filter(verified=True, display=True).all()[::-1]:
        if data.link:
            filename = browser.save(data.link, data.id)
            # data.link_image = filename + '.png'
            data.link_pdf = filename + '.pdf'
            data.save()

def get_data_from_feed(request):
    import feedparser
    import deepl

    NewsFeed = feedparser.parse(FEED_URL)
    titles = []
    for entry in NewsFeed.entries:
        print(entry)

        link = entry["link"].split("url=")[1]
        if Data.objects.filter(link=link).exists():
            continue
        file_name = entry["title"]
        organization = ""
        date_updated = dt = datetime.fromtimestamp(mktime(entry["updated_parsed"]))
        date_published = entry["updated_parsed"].tm_year
        month_published = entry["updated_parsed"].tm_mon
        country = "中国"
        province = ""
        municipality = ""

        translator = deepl.Translator(DEEPL_API)

        for cityi, provincei in city2province.items():
            if cityi in file_name:
                province = provincei
                municipality = cityi
                break
        for provincei in province2cities.keys():
            if provincei in file_name:
                province = provincei
                break


        result = translator.translate_text([file_name], target_lang='EN-US', source_lang='ZH')
        file_name_en = result[0]
        organization_en = ""
        country_en = "china"
        province_en = province_cn2en[province] if province in province_cn2en else ""
        municipality_en = city_cn2en[municipality] if municipality in city_cn2en else ""

        note = ""
        invalid_link = False

        data = Data(
            file_name_en=file_name_en,
            organization_en=organization_en,
            country_en=country_en,
            province_en=province_en,
            municipality_en=municipality_en,

            date_updated=date_updated,
            link=link,
            date_published=date_published,
            month_published=month_published,
            note=note,

            file_name=file_name,
            organization=organization,
            country=country,
            province=province,
            municipality=municipality,

            invalid_link=invalid_link,
        )
        data.save()

        # browser = Browser()
        # data.link_pdf = browser.save(data.link, data.id) + '.pdf'
        # data.save()

        titles.append(entry["title"])
    return HttpResponse(f'''Feed Url: <a href="{FEED_URL}">{FEED_URL}</a><br>
Successfully add {len(titles)} new data: {titles}''')


from django.views.generic import ListView


class ChinaView(ListView):
    queryset = Data.objects.filter(verified=True, display=True).exclude(country="").filter(province="").order_by("-date_published", "-month_published")
    template_name = "sino3060/china.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        map_data = list(
            Data.objects.filter(verified=True, display=True).exclude(province="")
            .filter(municipality="")
            .values("province")
            .annotate(name=F("province"), value=Count("province"))
            .values("name", "value")
        )
        print(map_data)
        context["map_data"] = json.dumps(map_data)
        return context


class ProvinceView(ListView):
    template_name = "sino3060/province.html"
    paginate_by = 20

    def get_queryset(self):
        province = self.request.GET.get("province", None)
        municipality = self.request.GET.get('municipality', None)
        if municipality is None:
            return Data.objects.filter(verified=True, display=True).filter(province=province, municipality="").order_by("-date_published", "-month_published")
        else:
            return Data.objects.filter(verified=True, display=True).filter(municipality=municipality).order_by("-date_published", "-month_published")

    def get_context_data(self, **kwargs):
        province = self.request.GET.get("province", None)

        context = super().get_context_data(**kwargs)
        map_data = list(
            Data.objects.filter(verified=True, display=True).exclude(municipality="")
            .filter(province=province)
            .values("municipality")
            .annotate(name=F("municipality"), value=Count("municipality"))
            .values("name", "value")
        )
        print(map_data)

        province = province[:2] if not province.startswith("黑龙江") and not province.startswith("内蒙古") else province[:3]
        province_en = ''.join(lazy_pinyin(province))

        context["map_data"] = json.dumps(map_data)
        context["province"] = json.dumps(province)
        context["province_en"] = json.dumps(province_en)
        context["province_en_url"] = json.dumps(f"https://assets.pyecharts.org/assets/v5/maps/{province_en}.js")
        return context

from django.contrib import admin
from .models import Data

from django import forms
from .constant import *
from .utils import *

FEED_URL = "https://www.google.com/alerts/feeds/01155419682148081808/11628317292397534831"
DEEPL_API = "b953cf0e-4320-da53-93fc-da67f7efc047:fx"
# DEEPL_API = "123ef762-e73f-4ed2-8a68-5a1830bdce64:fx"

class DataForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Data
        widgets = {
            'province': forms.Select(choices=[('', '')] + [(x, x) for x in province_cn2en.keys()]),
            'province_en': forms.Select(choices=[('', '')] + [(x, x) for x in province_cn2en.values()]),
        }

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
        date_updated = datetime.fromtimestamp(mktime(entry["updated_parsed"]))
        date_published = entry["updated_parsed"].tm_year
        month_published = entry["updated_parsed"].tm_mon
        country = "中国"
        province = ""
        municipality = ""
        county = ""

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


        result = translator.translate_text([file_name])
        file_name_en = result[0]
        organization_en = ""
        country_en = "china"
        province_en = province_cn2en[province] if province in province_cn2en else ""
        municipality_en = city_cn2en[municipality] if municipality in city_cn2en else ""
        county_en = ""

        note = ""
        invalid_link = False

        data = Data(
            file_name_en=file_name_en,
            organization_en=organization_en,
            country_en=country_en,
            province_en=province_en,
            municipality_en=municipality_en,
            county_en=county_en,

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
            county=county,

            invalid_link=invalid_link
        )
        data.save()

        browser = Browser()
        data.link_pdf = browser.save(data.link, data.id) + '.pdf'
        data.save()

        titles.append(entry["title"])
    print(f'ok with {len(titles)} new data: {titles}')

class DataAdmin(admin.ModelAdmin):
    form = DataForm
    # change_form_template = 'sino3060/change_form.html'
    # change_list_template = 'sino3060/change_list.html'
    search_fields = ['file_name_en', 'province_en', 'municipality_en', 'file_name', 'province', 'municipality']
    actions = [get_data_from_feed]


admin.site.register(Data, DataAdmin)

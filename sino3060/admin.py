from django.contrib import admin
from .models import Data

from django import forms

class DataForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Data
        widgets = {
            'province_en': forms.Select(choices=[('Anhui', 'Anhui'), ('Beijing', 'Beijing'), ('Chongqing', 'Chongqing'), ('Fujian', 'Fujian'), ('Gansu', 'Gansu'), ('Guangdong', 'Guangdong'), ('Guangxi', 'Guangxi'), ('Guizhou', 'Guizhou'), ('Hainan', 'Hainan'), ('Hebei', 'Hebei'), ('Heilongjiang', 'Heilongjiang'), ('Henan', 'Henan'), ('Hong Kong', 'Hong Kong'), ('Hubei', 'Hubei'), ('Hunan', 'Hunan'), ('Inner Mongolia', 'Inner Mongolia'), ('Jiangsu', 'Jiangsu'), ('Jiangxi', 'Jiangxi'), ('Jilin', 'Jilin'), ('Liaoning', 'Liaoning'), ('Macau', 'Macau'), ('Ningxia', 'Ningxia'), ('Qinghai', 'Qinghai'), ('Shaanxi', 'Shaanxi'), ('Shandong', 'Shandong'), ('Shanghai', 'Shanghai'), ('Shanxi', 'Shanxi'), ('Sichuan', 'Sichuan'), ('Tianjin', 'Tianjin'), ('Tibet', 'Tibet'), ('Xinjiang', 'Xinjiang'), ('Yunnan', 'Yunnan'), ('Zhejiang', 'Zhejiang')]),
            'province': forms.Select(choices=[("安徽省", "安徽省"), ("北京市", "北京市"), ("重庆市", "重庆市"), ("福建省", "福建省"), ("甘肃省", "甘肃省"), ("广东省", "广东省"), ("广西壮族自治区", "广西壮族自治区"), ("贵州省", "贵州省"), ("海南省", "海南省"), ("河北省", "河北省"), ("河南省", "河南省"), ("黑龙江省", "黑龙江省"), ("湖北省", "湖北省"), ("湖南省", "湖南省"), ("吉林省", "吉林省"), ("江苏省", "江苏省"), ("江西省", "江西省"), ("辽宁省", "辽宁省"), ("内蒙古自治区", "内蒙古自治区"), ("宁夏回族自治区", "宁夏回族自治区"), ("青海省", "青海省"), ("山东省", "山东省"), ("山西省", "山西省"), ("陕西省", "陕西省"), ("上海市", "上海市"), ("四川省", "四川省"), ("天津市", "天津市"), ("西藏自治区", "西藏自治区"), ("新疆维吾尔自治区", "新疆维吾尔自治区"), ("云南省", "云南省"), ("浙江省", "浙江省")])
        }


class DataAdmin(admin.ModelAdmin):
    form = DataForm


admin.site.register(Data, DataAdmin)

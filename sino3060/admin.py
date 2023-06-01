from django.contrib import admin
from .models import Data

from django import forms
from .constant import *
from .utils import *

class DataAdmin(admin.ModelAdmin):
    search_fields = ['file_name_en', 'province_en', 'municipality_en', 'file_name', 'province', 'municipality']


admin.site.register(Data, DataAdmin)

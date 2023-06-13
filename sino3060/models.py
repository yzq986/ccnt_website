from django.db import models

from .constant import *

class Data(models.Model):
    file_name_en = models.CharField(max_length=255)
    organization_en = models.CharField(max_length=255, blank=True)
    country_en = models.CharField(max_length=50, blank=True)
    province_en = models.CharField(max_length=50, blank=True, choices=sorted([('', '')] + [(x, x) for x in province_cn2en.values()]), default="", verbose_name="Province / Municipality")
    # municipality_en = models.CharField(max_length=50, choices=sorted([('', '')] + [(x, x) for x in city_cn2en.values()]), default=0)
    municipality_en = models.CharField(max_length=50, blank=True, verbose_name="County in province / District in municipality")
    
    date_updated = models.DateTimeField()
    link = models.URLField(max_length=255, blank=True)
    date_published = models.IntegerField(blank=True)
    month_published = models.IntegerField(blank=True)
    note = models.TextField(blank=True)

    file_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=50, blank=True)
    province = models.CharField(max_length=50, blank=True, choices=[('', '')] + [(x, x) for x in province_cn2en.keys()], default="", verbose_name="省 / 直辖市")
    # municipality = models.CharField(max_length=50, choices=[('', '')] + [(x, x) for x in city_cn2en.keys()], default=0)
    municipality = models.CharField(max_length=50, blank=True, verbose_name="市 / 直辖市区")
    
    # link_pdf = models.FileField(null=True, blank=True, upload_to='static/sino3060/', default=None)
    link_pdf = models.URLField(max_length=255, blank=True)

    verified = models.BooleanField(default=False)
    display = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.file_name_en}({self.file_name})"

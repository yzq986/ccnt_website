from django.db import models


class Data(models.Model):
    file_name_en = models.CharField(max_length=255)
    organization_en = models.CharField(max_length=255, blank=True, null=True)
    country_en = models.CharField(max_length=50, blank=True, null=True)
    province_en = models.CharField(max_length=50, blank=True, null=True)
    municipality_en = models.CharField(max_length=50, blank=True, null=True)
    county_en = models.CharField(max_length=50, blank=True, null=True)
    
    date_updated = models.DateTimeField(blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    date_published = models.IntegerField(blank=True, null=True)
    month_published = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    file_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    municipality = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    
    link_image = models.ImageField(null=True, blank=True, upload_to='static/sino3060/', default='static/sino3060/default.png')
    link_pdf = models.FileField(null=True, blank=True, upload_to='static/sino3060/', default=None)

    invalid_link = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.file_name_en}({self.file_name})"

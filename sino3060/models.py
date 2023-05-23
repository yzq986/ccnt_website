from django.db import models


class Data(models.Model):
    file_name_en = models.CharField(max_length=255)
    organization_en = models.CharField(max_length=255)
    country_en = models.CharField(max_length=50)
    province_en = models.CharField(max_length=50)
    municipality_en = models.CharField(max_length=50)
    county_en = models.CharField(max_length=50)
    date_updated = models.DateTimeField()
    link = models.URLField(max_length=255)
    date_published = models.IntegerField()
    month_published = models.IntegerField()
    note = models.TextField()

    file_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    
    link_image = models.ImageField(null=True, blank=True, upload_to='static/sino3060/', default='static/sino3060/default.png')
    link_pdf = models.FileField(null=True, blank=True, upload_to='static/sino3060/', default=None)

    invalid_link = models.BooleanField(default=False)

    def __str__(self):
        return self.file_name_en

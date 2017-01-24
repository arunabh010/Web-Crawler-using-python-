from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=128, unique= True)
#
#     def _unicode_(self):
#         return self.name
# #
# class Page(models.Model):
#     category = models.ForeignKey(Category)
#     title = models.CharField(max_length=128)
#     url= models.URLField()
#     views = models.IntegerField(default=0)

#define models for your RATINGS DB
class Ratings(models.Model):
    Name=models.CharField(max_length=66)
    Rating_Type=models.CharField
    Rating=models.CharField
    Rating_Date=models.CharField

    def __unicode__(self):
        return self.title

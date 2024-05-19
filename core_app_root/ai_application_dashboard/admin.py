from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Book)
admin.site.register(models.Category)
admin.site.register(models.Publisher)
admin.site.register(models.RecommendedBook)
admin.site.register(models.RecommendedBookCategory)
admin.site.register(models.RecommendedBookPublisher)
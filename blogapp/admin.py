from django.contrib import admin
from .models import article , author, category

# Register your models here.
class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","details"]
    class Mete:
        Model = author
admin.site.register(author,authorModel)

class articleModel(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__","details"]
    list_filter = ["posted_on","category"]
    class Mete:
        Model = article
admin.site.register(article,articleModel)

class categoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    
    class Mete:
        Model = category
admin.site.register(category,categoryModel)
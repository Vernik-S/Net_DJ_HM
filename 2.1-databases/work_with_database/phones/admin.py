from django.contrib import admin

# Register your models here.
from phones.models import Phone


@admin.register(Phone)
class PhonesAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    prepopulated_fields = {"slug": ("name",)}

# class ArticleAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#admin.site.register(Phone, PhonesAdmin)



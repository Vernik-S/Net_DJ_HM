from django.contrib import admin

# Register your models here.
from logistic.models import Product, Stock, StockProduct



class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "stocks"]
    list_editable = ['id']
    list_display_links = ["title", "stocks"]
    inlines = [StockProductInline]

@admin.register(Stock)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "address",]
    inlines = [StockProductInline]

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ["id", "stock", "product", "quantity", "price"]


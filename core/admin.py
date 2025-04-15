from django.contrib import admin
from .models import Category, Vendor, Product, ProductImage

class ProductImagesadmin(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'category', 'product_image')
    search_fields = ('title', 'category__title', 'user__username')
    list_filter = ('category', 'user')
    ordering = ('-id',)
    list_per_page = 6

class Categoryadmin(admin.ModelAdmin):
    list_display = ('title', 'category_image')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('-id',)
    list_per_page = 6

class Vendoradmin(admin.ModelAdmin):
    list_display = ('title', 'vendor_image')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('-id',)
    list_per_page = 6

admin.site.register(Category, Categoryadmin)
admin.site.register(Vendor, Vendoradmin)
admin.site.register(Product, ProductAdmin)
admin.site.site_header = "InnoWavz Admin"

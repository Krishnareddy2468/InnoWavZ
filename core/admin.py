from django.contrib import admin
from .models import category, Vendor, Product, ProductImage

class ProductImagesAdmin(admin.TabularInline):  # Renamed to follow PascalCase
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'category', 'product_image')
    search_fields = ('title', 'category__title', 'user__username')
    list_filter = ('category', 'user')
    ordering = ('-id',)
    list_per_page = 6
    inlines = [ProductImagesAdmin]  # Added inline for ProductImage

class CategoryAdmin(admin.ModelAdmin):  # Renamed to follow PascalCase
    list_display = ('title', 'category_image')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('-id',)
    list_per_page = 6

class VendorAdmin(admin.ModelAdmin):  # Renamed to follow PascalCase
    list_display = ('title', 'vendor_image')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('-id',)
    list_per_page = 6

admin.site.register(category, CategoryAdmin)  # Updated class name
admin.site.register(Vendor, VendorAdmin)  # Updated class name
admin.site.register(Product, ProductAdmin)
admin.site.site_header = "InnoWavz Admin"
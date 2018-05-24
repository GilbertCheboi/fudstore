from django.contrib import admin

from .models import Product, ProductFile, Category


#class ProductFileInline(admin.TabularInline):
 #   model = ProductFile
  #  extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    #inlines = [ProductFileInline]
    class Meta:
        model = Product, 

admin.site.register(Product,  ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    #inlines = [ProductFileInline]
    class Meta:
        model = Category, 
admin.site.register(Category,  CategoryAdmin)
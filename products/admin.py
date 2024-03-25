from django.contrib import admin
# class ProductAdmin(admin.ModelAdmin):
#     pass

from .models import Product,Test
# Register your models here.

# admin.site.register(ProductAdmin)
admin.site.register(Product)
admin.site.register(Test)
admin.site.site_header='Test'



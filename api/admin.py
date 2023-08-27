from django.contrib import admin
from .models import category, product, productLine, productImage, attribute, attributeValue

class categoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'get_category')
    
    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

class productLineAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'sku', 'stock_quantity', 'get_attributeValue')
    
    def get_attributeValue(self, obj):
        return [attributeValue.value for attributeValue in obj.attributeValue.all()]

class productImageAdmin(admin.ModelAdmin):
    list_display = ('productLine', 'name', 'alternative_text', 'url')

class attributeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class attributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'value')

admin.site.register(category, categoryAdmin)
admin.site.register(product, productAdmin)
admin.site.register(productLine, productLineAdmin)
admin.site.register(productImage, productImageAdmin)
admin.site.register(attribute, attributeAdmin)
admin.site.register(attributeValue, attributeValueAdmin)

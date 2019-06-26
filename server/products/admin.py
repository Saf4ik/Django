from django.contrib import admin
from django.template.loader import render_to_string
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified', 'created',)

    list_filter = ('modified', 'created', )

    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'picture', 'name', 'category', 'cost', 
        'modifield', 'created'
    )

    list_filter = ('category', 'modifield', 'created', )

    search_fields = ('name', 'description',)

    def picture(self, obj):
        return render_to_string(
            'components/picture.html',
            {'image': obj.image}
        )


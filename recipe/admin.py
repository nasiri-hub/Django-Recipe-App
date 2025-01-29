from django.contrib import admin
from .models import Recipe, Customer, Ingredient, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category']

    list_display = ['title', 'description',
                    'time', 'price', 'link', 'instructions']
    list_editable = ['price']
    list_per_page = 10
    list_select_related = ['category']
    date_hierarchy = 'time'
    ordering = ['title']

    class Media:
        css = {
            'all': ['recipe/styles.css']
        }


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['user__first_name', 'user__last_name']
    list_select_related = ['user']
    search_fields = ['user__first_name__istartswith',
                     'user__last_name__istartswith']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name']

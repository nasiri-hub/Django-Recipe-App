from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import TaggedItem
from recipe.admin import RecipeAdmin
from recipe.models import Recipe
from .models import User



@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'usable_password', 'password1', 'password2', 'email', 'first_name', 'last_name'),
            },
        ),
    )
    search_fields = ['first_name']


class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    extra = 0
    model = TaggedItem


class CustomRecipeAdmin(RecipeAdmin):
    inlines = [TagInline]


admin.site.unregister(Recipe)
admin.site.register(Recipe, CustomRecipeAdmin)
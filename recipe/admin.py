from django.contrib import admin
from . models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "ingredients", "instructions", "cooking_time", "servings", "type", "created_at"]
    search_fields = ("title",)
    list_filter = ["type"]

admin.site.register(Recipe, RecipeAdmin)



from django.contrib import admin
from . models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "ingredients", "instructions", "cooking_time", "servings", "type", "created_at", "image"]
    search_fields = ("title",)
    list_filter = ["type"]

admin.site.register(Recipe, RecipeAdmin)



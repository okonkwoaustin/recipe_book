from django.urls import path

from . import views

urlpatterns = [
    path("", views.recipe, name="index"),
    path("create_recipe/", views.create_recipe, name="create_recipe"),
    path("success", views.success, name="success"),
    path("recipes/<int:recipe_id>/", views.recipe_detail, name="recipe-detail"),
]